import glob
import zipfile

jars = glob.glob('*.jar')

for jar in jars:
    print '+ Processing ' + jar
    filtered_name = jar[:-4].lower().replace(' ', '').replace('_', '-')
    print '= Filtered name: ' + filtered_name
    z = zipfile.ZipFile(filtered_name + '.zip', 'w')
    z.write(jar, 'mods/' + jar, zipfile.ZIP_DEFLATED)
    z.close()
    print
