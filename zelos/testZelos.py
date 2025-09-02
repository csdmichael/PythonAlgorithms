import zelos_sdk

# Initialize once
zelos_sdk.init()

# Create logical sources
motor = zelos_sdk.TraceSource("motor_controller")
sensors = zelos_sdk.TraceSource("sensor_array")

# Log structured events
motor.log("status", {
    "state": "running",
    "rpm": 1500,
    "torque_nm": 25.5,
    "efficiency_percent": 92.3
})

# Write expressive hardware tests
def test_motor_acceleration(motor, check):
    """Verify motor reaches target speed within spec."""
    check.that(
        motor.status.rpm,
        "is greater than", 2000,
        within_duration_s=0.5
    )