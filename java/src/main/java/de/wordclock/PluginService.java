package de.wordclock;

import de.wordclock.plugin.wordclock.Plugin;
import org.springframework.scheduling.TaskScheduler;
import org.springframework.stereotype.Service;

import java.util.concurrent.ScheduledFuture;

import static java.util.Objects.isNull;

@Service
public class PluginService {
    private ScheduledFuture<?> actualScheduledPlugin;
    private final TaskScheduler executor;

    public PluginService(TaskScheduler executor) {
        this.executor = executor;
    }

    public void startPlugin(Plugin plugin, long rateInMs) {
        stopActualPlugin();
        actualScheduledPlugin = executor.scheduleAtFixedRate(plugin, rateInMs);
    }
 
    public void stopActualPlugin() {
        if (isNull(actualScheduledPlugin)) {
            return;
        }
        actualScheduledPlugin.cancel(true);
    }
}
