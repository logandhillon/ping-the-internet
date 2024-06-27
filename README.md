# Ping the Internet!

## What is this?

Ping the Internet! is a project made to ping ***every*** IPv4 address that could possibly exist, and see which ones respond to HTTP requests.
If an address is responding to an HTTP request, it can be viewed by a web browser, and is thus what we know as a "website."

Ultimately, it probes the vast landscapes of the internet, finding every website that exists in the process.

## Usage

Firstly, ensure you have the proper resources (computing power & time) to run this program. I would recommend running this on a dedicated machine, as it will use up to millions of threads, and is very heavy on system resources.

```sh
git clone https://github.com/logandhillon/ping-the-internet.git
cd ping-the-internet
```

Finally, run `probe_http.py`.

:warning: This script is **VERY** CPU-intensive, and sometimes may be difficult to abort! (even with task manager!)

## Disclaimer

Ping the Internet! is not liable nor responsible for any damages or other harm caused by the use of this program, its contents, or its output. This project will send out millions of network requests in a short amount of time, which *may* cause your router or ISP to temporarily disable internet access for your device or home.

**Irresponsible or improper use of this program may result in damages that YOU are solely liable for.**

## Licensing

© 2024 Logan Dhillon. See the full license at [LICENSE](LICENSE).
