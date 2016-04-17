# -*- coding: utf-8 -*-
import numpy as np

if __name__ == "__main__":
    infile = open("links.txt","r")
    page_dict = {}
    page_list = []
    count = 0
    for line in infile:
        fields = line.strip().split("\t")
        if fields[0] not in page_dict: 
            page_list.append(fields[0])
            page_dict[fields[0]] = [fields[1]]      #page_dict doesnot contain deadend as key
        else:
            page_dict[fields[0]].append(fields[1])
        if fields[1] not in page_dict:
            page_dict[fields[1]] = []
            page_list.append(fields[1])
    infile.close()
    
    deg_dict = {}
    length = len(page_list)
    rank_vec =  np.array([1.0/length] * length)
    for page in page_list:
        #print page_list.index(page)    
        deg_dict[page] = np.array([0.0] * length)
        out_degree = len(page_dict[page])
        #print out_degree
        for p in page_dict[page]:
            index = page_list.index(p)
            deg_dict[page][index] = 1.0/out_degree
            #print deg_dict[page][index]
        #print page_dict[page]
    #print deg_dict
    
    teleport = np.array([0.001] * length)
    for interation in range(50):
        rank_vec_next = np.array([0.0] * length)
        for page in page_list:
            index = page_list.index(page)
            rank_vec_next += deg_dict[page] * rank_vec[index]
            #print deg_dict[page]
            #print rank_vec[index]
            #print rank_vec_next
        rank_vec = 0.9*rank_vec_next + teleport
    

    ranks = np.sort(rank_vec)[::-1]
    stationary_ranks = rank_vec.tolist()
    top_10_ranks = ranks[0:10]
    for rank in top_10_ranks:
        index = stationary_ranks.index(rank)
        print page_list[index]
