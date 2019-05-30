package de.wordclock;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class WordclockController {

	@RequestMapping("/wordclock")
	public String wordClock() {
		LocalTimeProvider localTime = new LocalTimeProvider();
		WordClock wordClock = new WordClock();
		return wordClock.convertMinute(localTime.getMinutes());
	}
}
