import os
import sys
import winreg
import zipfile


class RwpInstaller:

    railworks_path = None

    def extract(self, target):
        with zipfile.ZipFile(target) as z:
            if z.testzip():
                return self.output('Corrupt file {}'.format(target))
            self.output('{} file valid'.format(target))
            z.extractall(self.railworks_path)
            self.output('{} extracted successfully'.format(target))

    def get_railworks_path(self):
        steam_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Valve\\Steam')
        steam_path = winreg.QueryValueEx(steam_key, 'SteamPath')[0]
        return os.path.join(steam_path, 'steamApps', 'common', 'railworks', 'plugins')

    def output(self, out, wait=False):
        if wait:
            input(out)
        else:
            print(out)

    def main(self):
        targets = sys.argv[1:]
        if not targets:
            return self.output('No RWP files passed.', wait=True)

        self.railworks_path = self.get_railworks_path()

        for target in targets:
            self.extract(target)

        self.output('All done. Thanks for using RWP Installer.', wait=True)


if __name__ == '__main__':
    RwpInstaller().main()
