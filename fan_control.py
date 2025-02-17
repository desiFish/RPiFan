# Import required libraries
import RPi.GPIO as GPIO  # For controlling Raspberry Pi GPIO pins
import time  # For adding delays in the loop

# Configuration constants
# GPIO18 (Pin 12) is being used for PWM fan control
FAN_PIN = 18
# Fan will turn on at full speed when temperature reaches 50°C
TEMP_HIGH = 50.0
# Fan will run at 50% when temperature is between 42°C and 50°C
TEMP_MEDIUM = 45.0
# Fan will stop completely when temperature drops below 42°C
TEMP_OFF = 42.0
# PWM frequency in Hz - determines how many times per second the signal switches
PWM_FREQ = 25


def setup():
    """
    Initialize GPIO settings and PWM
    Returns: PWM object for controlling the fan
    """
    GPIO.setmode(GPIO.BCM)  # Use Broadcom pin-numbering scheme
    GPIO.setup(FAN_PIN, GPIO.OUT)  # Set pin as output
    return GPIO.PWM(FAN_PIN, PWM_FREQ)  # Create PWM instance


def get_cpu_temp():
    """
    Read CPU temperature from system file
    Returns: CPU temperature in Celsius
    """
    # Read temperature from Raspberry Pi's thermal zone
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        # Convert temperature from millidegrees to degrees Celsius
        return float(f.read()) / 1000


def main():
    """
    Main program loop: monitors temperature and controls fan
    """
    try:
        fan = setup()  # Initialize GPIO and get PWM object
        fan.start(0)  # Start PWM with 0% duty cycle (fan off)

        while True:
            temp = get_cpu_temp()  # Get current CPU temperature

            # Temperature control logic
            if temp >= TEMP_HIGH:
                fan.ChangeDutyCycle(100)  # Full speed when hot
            elif temp >= TEMP_MEDIUM:
                fan.ChangeDutyCycle(50)  # Half speed when warm
            elif temp <= TEMP_OFF:
                fan.ChangeDutyCycle(0)  # Stop fan when cool

            time.sleep(2)  # Wait 2 seconds before next temperature check

    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print("\nStopping fan control")
    finally:
        # Clean up resources
        fan.stop()  # Stop PWM
        GPIO.cleanup()  # Release GPIO resources


# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
