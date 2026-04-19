# 029_MITM_Proxy - Intercepting HTTPS Traffic with a MITM Proxy

## Concept
Show how a man-in-the-middle proxy (mitmproxy) lets you intercept, inspect, and modify HTTPS traffic from apps and devices in real time.

## Key Points
- What a MITM proxy is and why HTTPS doesn't stop it when you control the device
- Set up mitmproxy and route traffic through it
- Install the mitmproxy CA certificate to defeat TLS validation
- Inspect API calls from a mobile app or CLI tool
- Modify a request on the fly and see the app react

## Hook
"Your app uses HTTPS. That won't stop me from reading every single request it makes."

## Practical Demo
- Start mitmproxy in terminal
- Configure a device / curl to use the proxy
- Browse to an HTTPS site — watch traffic appear in mitmproxy
- Intercept a request and modify the response body live
