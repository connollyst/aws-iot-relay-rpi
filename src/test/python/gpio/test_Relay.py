import unittest
from unittest.mock import MagicMock

from src.main.python.gpio.Relay import Relay


class test_Relay(unittest.TestCase):

    def test_should_create_relay_on(self):
        # Given
        relay = Relay(42, Relay.State.ON)
        # Then
        self.assertEqual(Relay.State.ON, relay.state)

    def test_should_create_relay_off(self):
        # Given
        relay = Relay(42, Relay.State.OFF)
        # Then
        self.assertEqual(Relay.State.OFF, relay.state)

    def test_should_initialize_relay_on(self):
        # Given
        mock_io = MagicMock()
        Relay(42, Relay.State.ON, mock_io)
        # Then
        mock_io.set_mode_bcm.assert_called()

    def test_should_initialize_relay_off(self):
        # Given
        mock_io = MagicMock()
        Relay(42, Relay.State.OFF, mock_io)
        # Then
        mock_io.set_mode_bcm.assert_called()

    def test_should_initialize_relay_on_pin_mode(self):
        # Given
        mock_io = MagicMock()
        Relay(42, Relay.State.ON, mock_io)
        # Then
        mock_io.set_pin_out.assert_called_with(42)

    def test_should_initialize_relay_off_pin_mode(self):
        # Given
        mock_io = MagicMock()
        Relay(42, Relay.State.OFF, mock_io)
        # Then
        mock_io.set_pin_out.assert_called_with(42)

    def test_should_initialize_relay_on_pin_state(self):
        # Given
        mock_io = MagicMock()
        Relay(42, Relay.State.ON, mock_io)
        # Then
        mock_io.output_high.assert_called_with(42)

    def test_should_initialize_relay_off_pin_state(self):
        # Given
        mock_io = MagicMock()
        Relay(42, Relay.State.OFF, mock_io)
        # Then
        mock_io.output_low.assert_called_with(42)

    def test_should_turn_relay_from_on_to_off(self):
        # Given
        mock_io = MagicMock()
        relay = Relay(42, Relay.State.ON, mock_io)
        # When
        relay.off()
        # Then
        mock_io.output_low.assert_called_with(42)

    def test_should_turn_relay_from_off_to_on(self):
        # Given
        mock_io = MagicMock()
        relay = Relay(42, Relay.State.OFF, mock_io)
        # When
        relay.on()
        # Then
        mock_io.output_high.assert_called_once_with(42)

    def test_should_turn_relay_from_on_to_on(self):
        # Given
        mock_io = MagicMock()
        relay = Relay(42, Relay.State.ON, mock_io)
        # When
        relay.on()
        # Then
        mock_io.output_high.assert_called_once_with(42)

    def test_should_turn_relay_from_off_to_off(self):
        # Given
        mock_io = MagicMock()
        relay = Relay(42, Relay.State.OFF, mock_io)
        # When
        relay.off()
        # Then
        mock_io.output_low.assert_called_once_with(42)


if __name__ == '__main__':
    unittest.main()
