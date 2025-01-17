# Live-Earth-Wallpapers
Set your Desktop background to near realtime picures of the earth. \
Supports all known **geostationary** satellites, high resolution **sentinel** images and Nasa **Solar Dynamics Observatory** Images!

<details>
<summary><h3>Installation for LINUX and MacOS</h3></summary>

1. `git clone https://github.com/L-Roth/Live-Earth-Wallpapers.git`
2. `cd Live-Earth-Wallpapers`
3. `./install.sh ["your choosen flags"]` Replace the brackets with all flags and arguments you want for your Script. For Options see [Script options](#scriptOptions)\
**Do not include the brackets!**
4. Check if crontab is installed: `crontab -l`
</details>
<details>
<summary><h3>Installation for Windows</h3></summary>

1. `git clone https://github.com/L-Roth/Live-Earth-Wallpapers.git`
2. setup a Windows-Task-Scheduler to run `changeBackground.py`. every 30 min.\
E.g.: `path_to_project/Live-Earth-Wallpapers/venv/bin/python3 path_to_project/Live-Earth-Wallpapers/changeBackground.py  -z 3 -s goes-16`
3. Use Programms like [backgroundswitcher](https://johnsad.ventures/software/backgroundswitcher/windows/) or [bionix](https://bionixwallpaper.com/desktop-wallpaper-app-download/) to periodicly change your background to the image `backgroundImage.png` in the project folder.
Make sure to update image 2-3 min. later than the TaskScheduler runs.
</details>

### Requirements
1. `crontab`
2. `python3`
3. `feh`, `nitrogen` or `gsettings` to update the background image

<details>
<summary><h3>Manual installation</h3></summary>

1. `git clone https://github.com/L-Roth/Live-Earth-Wallpapers.git`
2. `python3 -m venv venv`
3. `source venv/bin/activate`
4. `pip install -r requirements.txt`
5. Test installation with: `python3 /path/to/projectDir/changeBackground.py -z 0 -s meteosat-11`.
The Image `backgroundImage.png`should have updated. 
</details>
<details>
<summary><h3>Manually updating the Image</h3></summary>

Set a cronjob to execute the `changeBackground.py` script routinely:
1. execute `env | grep -i display` to find your exact DISPLAY name. (probably :0 or :0.0)
2. `*/30 * * * * DISPLAY=:{your display name from 1.} python3 /path/to/ProjectDir/changeBackground.py -z 3 -s meteosat-11 -p feh`

Example: `*/30 * * * * DISPLAY=:0 python3 /path/to/ProjectDir/changeBackground.py -z 3 -s meteosat-11 -p feh` \
To update the Background you need either `feh`, `nitrogen` or `gsettings` to be installed.
</details>

<h3 id="scriptOptions">Script Parameter Options:</h3>
<pre>usage: changeBackground.py [-h] [-z {0,1,2,3,4}] [-s {goes-16,goes-17,goes-18,himawari,meteosat-9,meteosat-11,sentinel,sdo}] [-p {feh,nitrogen,gsettings}] [-a LATITUDE] [-b LONGITUDE]

options:
  -h, --help            show this help message and exit
  -z {0,1,2,3,4}, --zoomLevel {0,1,2,3,4}
                        Change the ImageSize 0=678, 1=1356, 2=2712, 3=5424, 4=10848 (Meteosat does not support Level 4)
  -s {goes-16,goes-17,goes-18,himawari,meteosat-9,meteosat-11,sentinel,sdo}, --source {goes-16,goes-17,goes-18,himawari,meteosat-9,meteosat-11,sentinel,sdo}
                        Select Satellite as a source. goes-16, goes-17, goes-18, himawari, meteosat-9, meteosat-11, sentinel, sdo (NASA Solar Dynamics Observatory)
  -p {feh,nitrogen,gsettings}, --bgProgram {feh,nitrogen,gsettings}
                        Select Programm to set the Background.
  -a LATITUDE, --latitude LATITUDE
                        Set the latitude of the Background image bounding box you want to set. Only for Sentinel as source.
  -b LONGITUDE, --longitude LONGITUDE
                        Set the longitude of the Background image bounding box you want to set. Only for Sentinel as source.
</pre>

### Supported Satellites:
| **Satellite** | **Example image**                     |
|---------------|---------------------------------------|
| Sentinel      | ![alt text](examples/caribic.png)![alt text](examples/arctic.png)![alt text](examples/desert.png)|
| Goes-16       | ![alt text](examples/goes-16.png)     |
| Goes-17       | ![alt text](examples/goes-17.png)     |
| Goes-18       | ![alt text](examples/goes-18.png)     |
| Himamwari-8   | ![alt text](examples/himawari.png)    |
| Meteosat-9    | ![alt text](examples/meteosat-9.png)  |
| Meteosat-11   | ![alt text](examples/meteosat-11.png) |
| sdo           | ![alt text](examples/nasa_sdo.png) |

