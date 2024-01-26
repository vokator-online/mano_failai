import pyaudio
import numpy as np
import nvda.gui.guiHelper
import nvda.globalPlugins

# create an audio stream object
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=44100,
                output=True)

# define equalizer parameters
center_freqs = [100, 1000, 5000, 10000, 20000]
gain_factors = [1, 2, 1.5, 1.2, 0.8]
Q_values = [1, 2, 2, 1.5, 1]

# define a callback function that applies the equalizer effect
def equalizer_callback(data, gain_factors):
    # apply a bandpass filter at each center frequency
    for i, freq in enumerate(center_freqs):
        w0 = 2*np.pi*freq/44100
        alpha = np.sin(w0)/(2*Q_values[i])
        b = [alpha, 0, -alpha]
        a = [1 + alpha/Q_values[i], -2*np.cos(w0), 1 - alpha/Q_values[i]]
        data = np.convolve(data, b, mode='same')
        data = np.convolve(data, a, mode='same')
        # apply gain factor to the filtered signal
        data *= gain_factors[i]
    return data

# register the equalizer callback with NVDA
class Addon:
    def __init__(self):
        self.globalAddon = nvda.globalPlugins.addHandler(self)
    def terminate(self):
        self.globalAddon.removeHandler()
    def configDialog(self, parent):
        gui = nvda.gui.guiHelper.GuiBuilder(parent, _("Equalizer Settings"))
        slider_labels = [_("100Hz"), _("1kHz"), _("5kHz"), _("10kHz"),
_("20kHz")]
        slider_values = list(map(str, gain_factors))
        slider = gui.createSlider(_("Equalizer"), slider_labels, slider_values)
        def on_slider_change():
            for i in range(len(slider_values)):
                gain_factors[i] = float(slider_values[i])
        slider.onChange = on_slider_change
        return gui.getResult()

    def event_audioOutputChanged(self, speech, data):
        data = equalizer_callback(data, gain_factors)
        stream.write(data.astype(np.float32).tobytes())

addon = Addon()