# Import required libraries
import RPi.GPIO as GPIO  # For controlling Raspberry Pi GPIO pins
import time  # For adding delays in the loop

# Configuration constants
# GPIO12 is being used for PWM fan control
FAN_PIN = 12
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


def calculate_pwm_duty(temp, is_running):
    """
    Calculate PWM duty cycle based on temperature with hysteresis
    Returns: (PWM duty cycle percentage (0-100), new running state)
    """
    if temp >= TEMP_HIGH:
        return 100, True
    elif temp >= TEMP_MEDIUM:
        # Calculate proportional speed between 50% and 100%
        temp_range = TEMP_HIGH - TEMP_MEDIUM
        temp_offset = temp - TEMP_MEDIUM
        return (50 + (temp_offset / temp_range) * 50), True
    elif temp <= TEMP_OFF:
        return 0, False
    else:
        # Between TEMP_OFF and TEMP_MEDIUM, maintain previous state
        return (50 if is_running else 0), is_running


def main():
    """
    Main program loop: monitors temperature and controls fan
    """
    try:
        fan = setup()
        fan.start(0)
        is_running = False  # Track fan state

        while True:
            temp = get_cpu_temp()
            duty_cycle, is_running = calculate_pwm_duty(temp, is_running)
            fan.ChangeDutyCycle(duty_cycle)
            time.sleep(2)

    except KeyboardInterrupt:
        print("\nStopping fan control")
    finally:
        fan.stop()
        GPIO.cleanup()


# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
