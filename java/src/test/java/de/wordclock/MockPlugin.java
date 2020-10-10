package de.wordclock;

import de.wordclock.plugin.wordclock.Plugin;

public class MockPlugin implements Plugin {

    private final String pluginName;

    public MockPlugin(String pluginName) {
        this.pluginName = pluginName;
    }

    @Override
    public void run() {
        // nothing to do
    }

    @Override
    public String getPluginName() {
        return pluginName;
    }
}
