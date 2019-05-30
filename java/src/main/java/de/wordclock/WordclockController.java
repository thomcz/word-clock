package de.wordclock;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class WordclockController {
	@Autowired
	LocalTimeProvider localTime;

	@RequestMapping("/wordclock")
	public String wordClock() {
		return WordClockMinuten.convertMinute(localTime.getMinutes());
	}
}
