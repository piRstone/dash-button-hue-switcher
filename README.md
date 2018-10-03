# Dash Button Hue Switcher

Turn off your Philips Hue lights with an Amazon Dash Button 💡

## Setup

Gather the following informations:

### Find your Philips Hue Bridge IP address

Search the IP address in the settings of your Philips Hue app of in the iOS Home app.

### Find your Dash Button MAC address

According to [this Reddit post](https://www.reddit.com/r/raspberry_pi/comments/7knxsn/super_simple_amazon_dash_button_mac_address/), the easiest way to find the MAC address of your Dash Button if the following:

- Hold the button until the LED blinks blue
- From your iPhone or Android, connect to the "Amazon Configure Me" WiFi network that appears
- Open a web browser to this address: [http://192.168.0.1](http://192.168.0.1)
- You will see the Dash Button informations and its MAC address

### Connect your Amazon Dash Button to the WiFi network

According to [Amazon instructions](https://www.amazon.com/gp/help/customer/display.html?nodeId=201746340):

1. Open the Amazon Shopping app on your phone.
2. Tap the **Menu** icon within the Amazon app, and then select **Your Account**.
3. Under **Dash Devices**, select **Set up a new device**. If prompted to choose a device type, select Dash Button.
4. Read the terms and conditions. If you agree to them, tap **Agree & Get Started**.
5. Follow the prompts to connect the dash button to Wi-Fi.
6. **DON'T SELECT A PRODUCT AND QUIT THE SETUP**.
7. Go back to **Your Account** and under the **Dash Devices** section, tap **Manage devices > Notification Settings**.
8. **Disable all notifications to not be prompted to finish setup at each press of your button**.

### Register you Dash Button on you Philips Hue Bridge

To let your Dash Button control your lights, you must get a "username" to identify your object. To do so, execute in a shell:

```
curl http://192.168.1.x/api -X POST -d'{"devicetype":"dash"}'
```

You will get a response like this:

```
[
    {
        "success": {
            "username": "ENcrG6he3zC62KqE71FS6E4d4GSY7KPTPvEqb7bt"
        }
    }
]
```

Keep the **username**.

## Installation

Create a virtualenv with Python 3

`virtualenv venv -p python3`

Install dependencies

`pip3 install -r requirements.txt`

Run

`python3 listener.py <bridge_ip> <username> <mac_address>`

Where:

- `bridge-pi`: the local IP of your Philips Hue Bridge (192.168.1.xx)
- `username`: the Amazon Dash Button registered username previously saved
- `mac_address`: the Amazon Dash Button's MAC address

This program is meant to be run on a Raspberry Pi on the same network as the lights.

#### Sources

[https://www.journaldulapin.com/2016/12/19/amazon-dash-hue/](https://www.journaldulapin.com/2016/12/19/amazon-dash-hue/) (French)
