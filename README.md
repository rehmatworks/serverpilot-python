# ServerPilot Python Package
ServerPilot is an awesome tool to manage Ubuntu servers in order to run PHP (and other) web apps flawlessly. This is a Python package to interact with [ServerPilot API](https://serverpilot.io/docs/how-to-use-the-serverpilot-api).

## Installation
Install from PyPi:
```shell
pip install rwsp
```
or clone this repo and run:
```python
python setup.py install
```
### Usage
```python
from rwsp.serverpilot import ServerPilot
# Get API Creds at https://manage.serverpilot.io/account/api
clientId = '###############'
apiKey = '##############'
sp = ServerPilot(clientId, apiKey)
```

## Servers
#### List Servers
```python
sp.list_servers()
```

#### Get a Server
```python
serverId = 'ID of the server'
sp.get_server(serverId)
```

#### Create a Server
You will get server ID in response that you can use manually to configure your server
```python
data = {
    'name': 'mynewserver',
    'plan': 'business',
    'enable_ssh_password_auth': True
}
sp.create_server(data)
```

#### Update a Server
```python
data = {
    'plan': 'business',
    'firewall': True,
    'autoupdates': True,
    'deny_unknown_domains': True
}
serverId = 'ID of the server'
sp.update_server(serverId, data)
```

#### Delete a Server
This action will detach your server from your ServerPilot account.
```python
serverId = 'ID of the server'
sp.delete_server(serverId)
```

## Users
#### List Users
```python
sp.list_users()
```

#### Create a User
```python
data = {
    'name': 'mynewsshuser',
    'password': 'mysecurepassword'
}
serverId = 'ID of the server'
sp.create_user(serverId, data)
```

#### Get a User
```python
userId = 'ID of the SSH user'
sp.get_user(userId)
```
#### Update a User
You can update a user password.
```python
data = {
    'password': 'mynewsecurepassword'
}
userId = 'ID of the SSH user'
sp.update_user(userId, data)
```

#### Delete a User
```python
userId = 'ID of the SSH user'
sp.delete_user(userId)
```

## Apps
#### List Apps
```python
sp.list_apps()
```

#### Create a New App
```python
data = {
    'sysuserid': '####', # ID of the owner (SSH User)
    'name': 'myawesomeapp',
    'runtime': 'php7.2',
    'domains': ['mysite.com', 'www.mysite.com'],
    # Provide wordpress dictionary only if you need WP to be installed in your new app
    'wordpress': {
        'site_title': 'My WP Site',
        'admin_user': 'admin',
        'admin_password': 'mysecurepassword', # Min: 8, Max: 200
        'admin_email': 'admin@example.com'
    }
}
sp.create_app(data)
```

#### Get App Details
```python
appId = 'ID of the app'
sp.get_app(appId)
```

#### Update App Details
```python
data = {
    'runtime': 'php7.3',
    'domains': ['mysite.com', 'www.mysite.com', 'newsite.com', 'www.newsite.com']
}
appId = 'ID of the app'
sp.update_app(appId, data)
```

#### Enable / Install SSL
To enable `Auto-SSL`, don't pass the data object, just pass appId
```python
appId = 'ID of the app'
sp.enable_ssl(appId) # Throws an exception if SSL is already enabled
```

If you want to install a custom SSL, pass data with SSL assets
```python
appId = 'ID of the app'
data = {
    'key': 'privateKey',
    'cert': 'SSLCertContent',
    'cacerts': 'CACertsIfApplicable' # Optional
}
sp.enable_ssl(appId, data) # Throws an exception if already installed
```

#### Force SSL
```python
appId = 'ID of the app'
sp.force_ssl(appId) # Throws an exception if already forced
```

#### Disable SSL
This will uninstall / disable SSL (regardless of it is auto-ssl or custom)
```python
appId = 'ID of the app'
sp.disable_ssl(appId) # Throws an exception if already disabled
```

#### Delete an App
```python
appId = 'ID of the app'
sp.delete_app(appId)
```

### Databases
#### List Databases
```python
sp.list_databases()
```

#### Create a Database
```python
data = {
    'appid': 'appId', # ID of the app for which you are creating the database
    'name': 'databasename',
    'user': {
        'name': 'dbusername',
        'password': 'dbpassword'
    }
}
sp.create_database(data)
```

#### Get a Database
```python
databaseId = 'ID of the database'
sp.get_database(databaseId)
```

#### Update a Database
You can only update the user password for a database.
```python
data = {
    'user': {
        'password': 'newpassword'
    }
}
databaseId = 'ID of the database'
sp.update_database(databaseId, data)
```

#### Delete a Database
```python
databaseId = 'ID of the database'
sp.delete_database(databaseId)
```

## Actions
Each API call returns an action ID and you can use that ID to check the status of the concerned API call.
```python
actionId = 'ID of the action'
sp.check_action(actionId)
```

## Troubleshooting
Some of the most common errors you may encounter during utilizing this library are explained below:
* `Exception: 401 Error: Unauthorized` is thrown when API credentials are incorrect
* `Exception: 404 Error: Not Found` is thrown when you attempt to access a non-existent resource
* `Exception: 400 Error: Bad Request` is thrown generally when form parameters are invalid

This package covers all API operations supported by ServerPilot API. If you have any confusions on required parameters or something else, you should check the [API documentation of ServerPilot](https://github.com/ServerPilot/API).
