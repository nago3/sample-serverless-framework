# Serverless Framework - sample code -

that can be deployed without the need to provision or manage servers.

## Overview

The Serverless Framework is an open-source web framework for building applications
that can be deployed without the need to provision or manage servers.

## How to use

### import code

```shell
$ serverless install -u <GITHUB URL OF SERVICE>
```

### import packages

```shell
$ pip install -r requirements.txt
```

### commands

#### install plugins

``

```shell
$ sls plugin install -n <plugins>
```
#### deploy

`* Deploy when you change the code.`

```shell
$ sls deploy --aws-profile <your profile>
```

#### invoke

```shell
$ sls invoke -f <function name> --log --aws-profile <your profile>
```

`If you use test json data...`

1. Create `event.json` file
2. Execute the following command

```shell
$ sls invoke -f <function name> --log -p event.json --aws-profile <your profile>
```

## Version

- Framework Core: 3.38.0
- Plugin: 7.2.0
- SDK: 4.5.1

## URL

### official

https://www.serverless.com/framework

### document

https://www.serverless.com/framework/docs

### plugins

https://www.serverless.com/plugins
