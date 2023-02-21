# transmission-trackers-service
An automatic tracker addition service for Transmission 4.0 on Linux. this is inspired by [transmission-trackers](https://github.com/blind-oracle/transmission-trackers). This project is utilizing the new version of Transmission feature which allows you to add default trackers in the settings.

## Getting Started


You need the following dependencies to install this project:
* [Transmission](https://transmissionbt.com/) 4.0 or higher
* Python 3

To install, run:
```bash
sudo make install
```

To start the service, run:
```bash
sudo make enable_service
```

To uninstall, run:
```bash
sudo make uninstall
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

