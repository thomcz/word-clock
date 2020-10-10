package de.wordclock;

import de.wordclock.plugin.wordclock.Plugin;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.Spy;
import org.mockito.junit.jupiter.MockitoExtension;
import org.springframework.http.ResponseEntity;

import java.util.ArrayList;
import java.util.List;

import static org.assertj.core.api.Assertions.assertThat;
import static org.mockito.ArgumentMatchers.anyLong;
import static org.mockito.ArgumentMatchers.eq;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.verifyZeroInteractions;

@ExtendWith(MockitoExtension.class)
class WordclockRestControllerTest {
    private static final String MOCK_PLUGIN_NAME = "pluginName";

    @Mock
    private PluginService pluginService;

    @Spy
    private List<Plugin> plugins = new ArrayList<>();

    @InjectMocks
    private WordclockRestController wordclockRestController;

    @Test
    void startPlugin_noPluginFound() {
        PluginDto pluginDto = new PluginDto("abc");

        ResponseEntity<String> stringResponseEntity = wordclockRestController.startPlugin(pluginDto);

        verifyZeroInteractions(pluginService);
        assertThat(stringResponseEntity.getBody()).contains("no plugin found with name");
        assertThat(stringResponseEntity.getBody()).contains("abc");
    }

    @Test
    void startPlugin_pluginFound() {
        PluginDto pluginDto = new PluginDto(MOCK_PLUGIN_NAME);
        MockPlugin plugin = new MockPlugin(MOCK_PLUGIN_NAME);
        plugins.add(plugin);

        ResponseEntity<String> stringResponseEntity = wordclockRestController.startPlugin(pluginDto);

        verify(pluginService).startPlugin(eq(plugin), anyLong());
        assertThat(stringResponseEntity.getBody()).contains("started plugin with name");
        assertThat(stringResponseEntity.getBody()).contains(MOCK_PLUGIN_NAME);
    }

    @Test
    void stop() {
        ResponseEntity<String> stringResponseEntity = wordclockRestController.stop();
        
        verify(pluginService).stopActualPlugin();
        assertThat(stringResponseEntity.getBody()).contains("stopped actual running plugin");
    }
}