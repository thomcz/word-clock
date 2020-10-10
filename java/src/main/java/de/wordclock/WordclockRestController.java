package de.wordclock;

import de.wordclock.plugin.wordclock.Plugin;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;
import java.util.Optional;

@RestController
public class WordclockRestController {
    private final List<Plugin> plugins;
    private final PluginService pluginService;

    private static final long SCHEDULER_RATE_IN_MS = 1000L;

    public WordclockRestController(List<Plugin> plugins, PluginService pluginService) {
        this.plugins = plugins;
        this.pluginService = pluginService;
    }

    @PostMapping("/startPlugin")
    public ResponseEntity<String> startPlugin(@RequestBody PluginDto pluginDto) {
        Optional<Plugin> pluginOptional = plugins.stream().filter(p -> p.getPluginName().equals(pluginDto.getPluginName())).findFirst();
        if (pluginOptional.isPresent()) {
            pluginService.startPlugin(pluginOptional.get(), SCHEDULER_RATE_IN_MS);
            return ResponseEntity.ok("started plugin with name: " + pluginDto.getPluginName());
        }
        return ResponseEntity.ok("no plugin found with name: " + pluginDto.getPluginName());

    }
 
    @PostMapping("/stopPlugin")
    public ResponseEntity<String> stop() {
        pluginService.stopActualPlugin();
        return ResponseEntity.ok("stopped actual running plugin");
    }
}
