package de.wordclock;

import de.wordclock.plugin.wordclock.Plugin;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;

import static org.hamcrest.CoreMatchers.containsString;
import static org.mockito.Mockito.*;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@WebMvcTest(WordclockRestController.class)
class WordclockRestControllerSystemTest {
    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private PluginService pluginService;

    @MockBean
    private Plugin plugin;

    private static final String INVALID_PLUGIN_NAME = "abs";
    private static final String MOCK_PLUGIN_NAME = "mockPlugin";

    @Test
    public void startPlugin_shouldNotFindPlugin() throws Exception {
        String content = "{\"pluginName\":\""+ INVALID_PLUGIN_NAME +"\"}";
        when(plugin.getPluginName()).thenReturn(MOCK_PLUGIN_NAME);

        this.mockMvc.perform(
                post("/startPlugin").contentType(MediaType.APPLICATION_JSON).content(content))
                .andExpect(status().isOk())
                .andExpect(content().string(containsString("no plugin found with name")))
                .andExpect(content().string(containsString(INVALID_PLUGIN_NAME)));
    }

    @Test
    public void startPlugin_shouldFindPluginWithName() throws Exception {
        String content = "{\"pluginName\":\""+ MOCK_PLUGIN_NAME +"\"}";
        when(plugin.getPluginName()).thenReturn(MOCK_PLUGIN_NAME);

        this.mockMvc.perform(
                post("/startPlugin").contentType(MediaType.APPLICATION_JSON).content(content))
                .andExpect(status().isOk())
                .andExpect(content().string(containsString("started plugin with name")))
                .andExpect(content().string(containsString(MOCK_PLUGIN_NAME)));
    }

    @Test
    public void stopPlugin() throws Exception {
        this.mockMvc.perform(
                post("/stopPlugin"))
                .andExpect(status().isOk())
                .andExpect(content().string(containsString("stopped actual running plugin")));
    }

}