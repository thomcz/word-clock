package de.wordclock;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

import de.wordclock.plugin.wordclock.Plugin;

@RestController
public class WordclockController {
	private final Plugin wordClock;
	private final PluginService pluginService;

	public WordclockController(Plugin wordClock, PluginService pluginService) {
		this.wordClock = wordClock;
		this.pluginService = pluginService;
	}

	@PostMapping("/wordclock")
	public void wordClock() {
		pluginService.startPlugin(wordClock, 1000);
	}

	@PostMapping("/stop")
	public void stop() {
		pluginService.stopActualPlugin();
	}
}
