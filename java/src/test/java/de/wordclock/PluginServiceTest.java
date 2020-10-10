package de.wordclock;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import org.springframework.scheduling.TaskScheduler;

import static org.mockito.Mockito.verify;

@ExtendWith(MockitoExtension.class)
class PluginServiceTest {
    private static final int SCHEDULER_RATE = 1000;
    private static final String MOCK_PLUGIN_NAME = "pluginName";
    @Mock
    private TaskScheduler executor;

    @InjectMocks
    private PluginService pluginService;

    @Test
    void test() {
        MockPlugin plugin = new MockPlugin(MOCK_PLUGIN_NAME);
        pluginService.startPlugin(plugin, SCHEDULER_RATE);

        verify(executor).scheduleAtFixedRate(plugin, SCHEDULER_RATE);
    }
}