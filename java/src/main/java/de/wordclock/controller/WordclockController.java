package de.wordclock.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import de.wordclock.plugin.wordclock.Plugin;

@RestController
public class WordclockController {
	@Autowired
	private Plugin wordClock;
	private Thread thread;

	@RequestMapping("/wordclock")
	public void wordClock() {
		thread = new Thread(wordClock);
		thread.start();
	}

	@RequestMapping("/stop")
	public void stop() {
		thread.interrupt();
	}
}
