import tkinter as tk
from tkinter import ttk
import sounddevice as sd
import numpy as np
import wave
import os

class VoiceRecorderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Recorder")

        self.record_button = ttk.Button(root, text="Record", command=self.toggle_recording)
        self.record_button.grid(row=0, column=0, padx=10, pady=10)

        self.save_button = ttk.Button(root, text="Save", command=self.save_recording, state="disabled")
        self.save_button.grid(row=0, column=1, padx=10, pady=10)

        self.recording = False
        self.frames = []
        self.filename = ""

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def toggle_recording(self):
        if not self.recording:
            self.start_recording()
        else:
            self.stop_recording()

    def start_recording(self):
        self.recording = True
        self.frames = []
        self.filename = ""
        self.record_button.configure(text="Stop Recording", style="Red.TButton")
        self.save_button.configure(state="disabled")

        def callback(indata, frames, time, status):
            if status:
                print('Error:', status)
            self.frames.append(indata.copy())

        with sd.InputStream(callback=callback):
            self.root.mainloop()

    def stop_recording(self):
        self.recording = False
        self.record_button.configure(text="Record", style="TButton")
        self.save_button.configure(state="enabled")

    def save_recording(self):
        if self.frames:
            self.filename = self.get_filename()
            with wave.open(self.filename, 'wb') as wf:
                wf.setnchannels(2)
                wf.setsampwidth(2)
                wf.setframerate(44100)
                wf.writeframes(b''.join(self.frames))

            self.frames = []
            self.save_button.configure(state="disabled")
            print("Recording saved:", self.filename)

    def get_filename(self):
        index = 1
        while True:
            filename = f"recording_{index}.wav"
            if not os.path.exists(filename):
                return filename
            index += 1

    def on_close(self):
        if self.recording:
            self.stop_recording()
        self.root.destroy()

def main():
    root = tk.Tk()
    style = ttk.Style()
    style.configure("Red.TButton", foreground="red")
    app = VoiceRecorderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
