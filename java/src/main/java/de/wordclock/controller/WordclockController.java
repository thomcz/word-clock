package de.wordclock.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

import de.wordclock.plugin.wordclock.Plugin;

@RestController
public class WordclockController {
	@Autowired
	private Plugin wordClock;
	private Thread thread;

	@PostMapping("/wordclock")
	public void wordClock() {
		startPlugin(wordClock);
	}

	@PostMapping("/stop")
	public void stop() {
		if (thread != null) {
			thread.interrupt();
		}
	}

	private void startPlugin(Plugin plugin) {
		if (thread != null) {
			thread.interrupt();
		}
		thread = new Thread(plugin);
		thread.start();

	}
}
