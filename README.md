# ARTSS
ARTSS data visualisation web application

## Installation

Use the [git clone](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-clone) to install ARTSS. Then use Python IDE of your choice to run localhost version of application.
Make sure all the necessary libraries from `requirements.txt` has been installed using [pip](https://pip.pypa.io/en/stable/).
```bash
git clone https://github.com/zanis-timsans/ARTSS
pip install library_name
```

## Usage
Use together with Moodle ARTSS xAPI plugin.

Update dropdown with your API link.
```python
dcc.Dropdown(options=[
                {'label': 'Your course',
                 'value': 'API link'},
```

## Contributing
Pull requests are welcome when authorized. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
Copyright (C) RTU Distance Education Study Center - All Rights Reserved
Unauthorized copying of this file, via any medium is strictly prohibited
Proprietary and confidential
Part of the [ARTSS project](https://artss.rtu.lv/)
Written by Zanis Timsans <zanis.timsans@gmail.com>, December 2020
