#INF360 - Programming in Python
#Lauren Robben
#Assignment 4
import zipfile, os

   def backupToZip(folder):
       # Back up the entire contents of "folder" into a ZIP file.

       folder = os.path.abspath(folder)   # make sure folder is absolute

       # Figure out the filename this code should use based on
       # what files already exist.
    number = 1
    while True:
           zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
           if not os.path.exists(zipFilename):
               break
           number = number + 1

#Create the ZIP file.

#Walk the entire folder tree and compress the files in each folder.
       print('Done.')
#Create the ZIP file.
    print(f'Creating{zipLaurenRobbenAssignment4}...')
      backupZip = zipfile.ZipFile(zipLaurenRobbenAssignment4, 'w')

     # TODO: Walk the entire folder tree and compress the files in each folder.
     print('Done.')

#Walk the entire folder tree and compress the files in each folder.
  for foldername, subfolders, filenames in os.walk(folder):
         print(f'Adding files in {Assignment4}...')
         # Add the current folder to the ZIP file.
      backupZip.write(Assignment4)

         # Add all the files in this folder to the ZIP file.
      for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue   # don't back up the backup ZIP files
             backupZip.write(os.path.join(Assignment4, LaurenRobbenAssignment4))
     backupZip.close()
     print('Done.')



#MadLibs Game
#Questions Go Here
noun1 = input('Enter a noun:')
adj1 = input('Enter an adjective:')
adverb1 = input('Enter an adverb:')
verb1 = input('Enter a verb:')
noun2 = input('Enter another noun:')
adj2 = input('Enter another adjective:')
adverb2 = input('Enter another adverb:')
verb2 = input('Enter another verb:')

#MadLib prints out below
print('There are many ' + adj1 + ' ways to choose a/an ' + noun1 + 'to swim.')
print(
