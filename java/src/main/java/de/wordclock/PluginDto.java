package de.wordclock;

public class PluginDto {
    private String pluginName;

    public PluginDto() {
    }

    public PluginDto(String pluginName) {
        this.pluginName = pluginName;
    }

    public String getPluginName() {
        return pluginName;
    }

    public void setPluginName(String pluginName) {
        this.pluginName = pluginName;
    }
}
