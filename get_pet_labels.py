#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#
# PROGRAMMER:
# DATE CREATED:
# REVISED DATE:
# PURPOSE: Create the function get_pet_labels that creates the pet labels from
#          the image's filename. This function inputs:
#           - The Image Folder as image_dir within get_pet_labels function and
#             as in_arg.dir for the function call within the main function.
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main.
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0: pet image label (string).
#
##
# Imports python modules
from os import listdir


def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames
    of the image files. These pet image labels are used to check the accuracy
    of the labels that are returned by the classifier function since the
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a
      List. The list contains the following item:
         index 0 = pet image label (string)
    """
# List the filenames in the image_dir
    filenames = listdir(image_dir)
    
    # Initialize an empty list for pet labels

    results_dic = dict()
    for file_name in filenames:
      if file_name[0] != ".":  
        low_pet_image = file_name.lower()
        word_list_pet_image = low_pet_image.split("_")
        pet_name = ""
        for word in word_list_pet_image:
            if word.isalpha():
              pet_name += word + " "
        pet_name = pet_name.strip()
        
        if file_name not in results_dic:
                results_dic[file_name] = [pet_name]
        else:
            print("** Warning: Key=", file_name, 
                "already exists in results_dic with value =", 
                results_dic[file_name])
    return results_dic

'''
    
 # Load dog names from 'dognames.txt'
   """ with open('dognames.txt', 'r') as file:
       dog_names = [line.strip() for line in file]"""
    # Open the file for reading
    with open('dognames.txt', 'r') as file:
        for line in file:
            name = line.strip()
            pet_labels.append(name)

    # Iterate through the filenames and pet labels to populate the results_dic
    for idx in range(0, len(filenames)):
        # Check if the filename is not already in the results_dic
        if filenames[idx] not in results_dic:
            # Add the filename as the key and a list containing the pet label as the value
            results_dic[filenames[idx]] = [pet_labels[idx]]
        else:
            print("** Warning: Key=", filenames[idx], "already exists in results_dic with value =",results_dic[filenames[idx]]

    # Iterating through the dictionary to print all key-value pairs
   # print("\nPrinting all key-value pairs in dictionary results_dic:")
    for key in results_dic:
        print("Filename=", key, "   Pet Label=", results_dic[key][0])
'''
 
