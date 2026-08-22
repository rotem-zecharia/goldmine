# dolthub/dolt

Dolt – Git for Data

## installation

Dolt is a single ~103 megabyte program. 

```bash
dolt $ du -h /Users/timsehn/go/bin/dolt
103M	/Users/timsehn/go/bin/dolt
```

It's really easy to install. Download it and put it on your `PATH`. 
We have a bunch of ways to make this even easier for most platforms.

## configuration

Verify that your installation has succeeded by running `dolt` in your
terminal.

```
$ dolt
Valid commands for dolt are
[...]
```

Configure `dolt` with your user name and email, which you'll need to
create commits. The commands work exactly the same as git.

```
$ dolt config --global --add user.email YOU@DOMAIN.COM
$ dolt config --global --add user.name "YOUR NAME"
```
