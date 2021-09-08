import unittest
from unittest.mock import MagicMock

from src.main.python.Logger import get_logger
from src.main.python.gpio.Relay import Relay


class test_Relay(unittest.TestCase):
    logger = get_logger('test')

    def test_should_create_relay_on(self):
        # Given
        relay = Relay(42, Relay.State.ON, logger=self.logger)
        # Then
        self.assertEqual(Relay.State.ON, relay.state)

    def test_should_create_relay_off(self):
        # Given
        relay = Relay(42, Relay.State.OFF, logger=self.logger)
        # Then
        self.assertEqual(Relay.State.OFF, relay.state)

    def test_should_initialize_relay_on(self):
        # Given
        mock_io = MagicMock()
        Relay(42, Relay.State.ON, gpio=mock_io, logger=self.logger)
        # Then
        mock_io.set_mode_bcm.assert_called()

    def test_should_initialize_relay_off(self):
        # Given
        mock_io = MagicMock()
        Relay(42, Relay.State.OFF, gpio=mock_io, logger=self.logger)
        # Then
        mock_io.set_mode_bcm.assert_called()

    def test_should_initialize_relay_on_pin_mode(self):
        # Given
        mock_io = MagicMock()
        Relay(42, Relay.State.ON, gpio=mock_io, logger=self.logger)
        # Then
        mock_io.set_pin_out.assert_called_with(42)

    def test_should_initialize_relay_off_pin_mode(self):
        # Given
        mock_io = MagicMock()
        Relay(42, Relay.State.OFF, gpio=mock_io, logger=self.logger)
        # Then
        mock_io.set_pin_out.assert_called_with(42)

    def test_should_initialize_relay_on_pin_state(self):
        # Given
        mock_io = MagicMock()
        Relay(42, Relay.State.ON, gpio=mock_io, logger=self.logger)
        # Then
        mock_io.output_high.assert_called_with(42)

    def test_should_initialize_relay_off_pin_state(self):
        # Given
        mock_io = MagicMock()
        Relay(42, Relay.State.OFF, gpio=mock_io, logger=self.logger)
        # Then
        mock_io.output_low.assert_called_with(42)

    def test_should_turn_relay_from_on_to_off(self):
        # Given
        mock_io = MagicMock()
        relay = Relay(42, Relay.State.ON, gpio=mock_io, logger=self.logger)
        # When
        relay.off()
        # Then
        mock_io.output_low.assert_called_with(42)

    def test_should_turn_relay_from_off_to_on(self):
        # Given
        mock_io = MagicMock()
        relay = Relay(42, Relay.State.OFF, gpio=mock_io, logger=self.logger)
        # When
        relay.on()
        # Then
        mock_io.output_high.assert_called_once_with(42)

    def test_should_turn_relay_from_on_to_on(self):
        # Given
        mock_io = MagicMock()
        relay = Relay(42, Relay.State.ON, gpio=mock_io, logger=self.logger)
        # When
        relay.on()
        # Then
        mock_io.output_high.assert_called_once_with(42)

    def test_should_turn_relay_from_off_to_off(self):
        # Given
        mock_io = MagicMock()
        relay = Relay(42, Relay.State.OFF, gpio=mock_io, logger=self.logger)
        # When
        relay.off()
        # Then
        mock_io.output_low.assert_called_once_with(42)

    def test_should_print_json_for_relay_on(self):
        # Given
        relay = Relay(42, Relay.State.ON, gpio=MagicMock(), logger=self.logger)
        # When
        json = relay.to_json()
        # Then
        self.assertEqual('ON', json['reading']['value'])

    def test_should_print_json_for_relay_off(self):
        # Given
        relay = Relay(42, Relay.State.OFF, gpio=MagicMock(), logger=self.logger)
        # When
        json = relay.to_json()
        # Then
        self.assertEqual('OFF', json['reading']['value'])


if __name__ == '__main__':
    unittest.main()
