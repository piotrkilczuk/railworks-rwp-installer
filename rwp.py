import os
import sys
import winreg
import zipfile


class RwpInstaller:

    railworks_path = None

    def extract(self, target):
        with zipfile.ZipFile(target) as z:
            if z.testzip():
                return self.output('Corrupt file {}\n'.format(target))
            self.output('{} file valid\n\n'.format(target))

            extracted = 0
            to_be_extracted = len(z.infolist())
            for file in z.infolist():
                extracted_path = z.extract(file, self.railworks_path).replace(self.railworks_path, '')
                extracted += 1

                percent_complete = extracted / to_be_extracted
                self.output('[{}/{} {}] {}\r'.format(
                    extracted, to_be_extracted,
                    (round(percent_complete * 10) * '*').ljust(10),
                    extracted_path[-55:]))

            self.output('\n\n{} extracted successfully'.format(os.path.basename(target)))

    def get_railworks_path(self):
        steam_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Valve\\Steam')
        steam_path = winreg.QueryValueEx(steam_key, 'SteamPath')[0]
        return os.path.join(steam_path, 'steamApps', 'common', 'railworks')

    def output(self, out, wait=False):
        if wait:
            input(out)
        else:
            sys.stdout.write(out)

    def main(self):
        targets = sys.argv[1:]
        if not targets:
            return self.output('No RWP files passed.', wait=True)

        self.railworks_path = self.get_railworks_path()

        for target in targets:
            self.extract(target)

        self.output('\n\nAll done. Thanks for using RWP Installer.', wait=True)


if __name__ == '__main__':
    RwpInstaller().main()
