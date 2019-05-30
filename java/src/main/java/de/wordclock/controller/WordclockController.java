package de.wordclock.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import de.wordclock.plugin.wordclock.WordClock;

@RestController
public class WordclockController {
	@Autowired
	private WordClock wordClock;

	@RequestMapping("/wordclock")
	public String wordClock() {
		return wordClock.getConvertedTime();
	}
}
