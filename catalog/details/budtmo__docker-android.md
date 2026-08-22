# budtmo/docker-android

Android in docker solution with noVNC supported and video recording

## requirements

1. Docker is installed on your system.

## installation

1. If you use ***Ubuntu OS*** on your host machine, you can skip this step. For ***OSX*** and ***Windows OS*** user, you need to use Virtual Machine that support Virtualization with Ubuntu OS because the image can be run under ***Ubuntu OS only***.

2. Your machine should support virtualization. To check if the virtualization is enabled is:
    ```
    sudo apt install cpu-checker
    kvm-ok
    ```

3. Run Docker-Android container
    ```
    docker run -d -p 6080:6080 -e EMULATOR_DEVICE="Samsung Galaxy S10" -e WEB_VNC=true --device /dev/kvm --name android-container budtmo/docker-android:emulator_11.0
    ```

4. Open ***http://localhost:6080*** to see inside running container.

5. To check the status of the emulator
    ```
    docker exec -it android-container cat device_status
    ```

Persisting data
-----------

The default behaviour is to destroy the emulated device on container restart. To persist data, you need to mount a volume at `/home/androidusr`:
    ```
    docker run -v data:/home/androidusr budtmo/docker-android:emulator_11.0
    ```

WSL2 Hardware acceleration (Windows 11 only)
-----------

Credit goes to [Guillaume - The Parallel Interface blog](https://www.paralint.com/2022/11/find-new-modified-and-unversioned-subversion-files-on-windows)

[Microsoft - Advanced settings configuration in WSL](https://learn.microsoft.com/en-us/windows/wsl/wsl-config)


1. Add yourself to the `kvm` usergroup.
    ```
    sudo usermod -a -G kvm ${USER}
    ```

2. Add necessary flags to `/etc/wsl.conf` to their respective sections.
    ```
    [boot]
    command = /bin/bash -c 'chown -v root:kvm /dev/kvm && chmod 660 /dev/kvm'
    ```

    Then, using PowerShell, open a notepad on `notepad $env:USERPROFILE\.wslconfig`. Inside, put these other flags:
    ```
    [wsl2]
    nestedVirtualization=true
    ```

4. Restart WSL2 via CMD prompt or Powershell
    ```
    wsl --shutdown
    ```


`command = /bin/bash -c 'chown -v root:kvm /dev/kvm && chmod 660 /dev/kvm'` sets `/dev/kvm` to `kvm` usergroup rather than the default `root` usergroup on WSL2 startup.

`nestedVirtualization` flag is only available to Windows 11.

If this setup does not work, you may have an old WSL version. In that case, ignore `\.wslconfig` and put everything on `/etc/wsl.conf`, including the `[wsl2]` flag.

## configuration

This [document](./documentations/CUSTOM_CONFIGURATIONS.md) contains information about configurations that can be used to enable some features, e.g. log-sharing, etc.
