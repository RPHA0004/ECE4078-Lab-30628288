import os
import shutil
def rename_file(i, script_dir):
    save_path = 'Group405_final/'
    new_dir = os.path.join(script_dir,save_path)
    old_slam = "slam.txt"
    old_targets = "targets.txt"
    new_slam = "slam_run{}_405.txt".format(i)
    new_targets = "targets_run{}_405.txt".format(i)
    shutil.copy2(old_slam, os.path.join(new_dir, new_slam))
    shutil.copy2(old_targets, os.path.join(new_dir, new_targets))

if __name__ == '__main__':
    os.chdir('lab_output/')
    script_dir = os.getcwd()
    input = input("run number: ")
    input = int(input)
    rename_file(input, script_dir)

    



