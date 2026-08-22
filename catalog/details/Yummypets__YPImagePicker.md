# Yummypets/YPImagePicker

📸 Instagram-like image picker & filters for iOS

## features

🌅 Library  
📷 Photo  
🎥 Video  
✂️ Crop  
⚡️ Flash  
🖼 Filters  
📁 Albums  
🔢 Multiple Selection  
📏 Video Trimming & Cover selection  
📐 Output image size  
And many more...

## installation

#### Using [CocoaPods](http://cocoapods.org/)

First, be sure to run `pod repo update` to get the latest version available.

Add `pod 'YPImagePicker'` to your `Podfile` and run `pod install`. Also, add `use_frameworks!` to the `Podfile`.

```
target 'MyApp'
pod 'YPImagePicker'
use_frameworks!
```

#### Using [Swift Package Manager](https://swift.org/package-manager/)

Open SPM dependency manager through `File > Swift Packages > Add Package Dependency...`.

and insert repository URL:

``https://github.com/Yummypets/YPImagePicker.git``

To add dependency in your own package, just specify a package in dependencies of your `Package.swift`:
```swift
.package(
name: "YPImagePicker",
url: "https://github.com/Yummypets/YPImagePicker.git",
.upToNextMajor(from: "5.0.0")

## configuration

All the configuration endpoints are in the [YPImagePickerConfiguration](https://github.com/Yummypets/YPImagePicker/blob/master/Source/Configuration/YPImagePickerConfiguration.swift) struct.
Below are the default value for reference, feel free to play around :)

```swift
var config = YPImagePickerConfiguration()
// [Edit configuration here ...]
// Build a picker with your configuration
let picker = YPImagePicker(configuration: config)
```

## tools

First things first `import YPImagePicker`.  

The picker only has one callback `didFinishPicking` enabling you to handle all the cases. Let's see some typical use cases 🤓
