import sys
import MySQLdb

db = MySQLdb.connect(
    host="localhost", user="root", passwd="root", db="playground")

def get_tree():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM nstree")
    rows = cursor.fetchall()
    cursor.close()
    d = []
    for row in rows:
    	d.append({
    		"id": int(row[0]),
    		"left": int(row[1]),
    		"right": int(row[2]),
    		"value": row[3]
    	})

    return d

def insert_node_next_to(left_name, name):
    cursor = db.cursor()

    rows = (0, )
    if(left_name is not None):
    	cursor.execute("SELECT nsright FROM nstree WHERE value = '%s' " % (str(left_name), ))
    	rows = cursor.fetchone()
 
    bright = rows[0] 

    # fill the space and shift the right side
    cursor.execute("UPDATE nstree SET nsright = nsright + 2 WHERE nsright > " + str(bright))
    cursor.execute("UPDATE nstree SET nsleft = nsleft + 2 WHERE nsleft > " + str(bright))

    cursor.execute("INSERT INTO nstree SET nsleft = %d, nsright = %d, value = '%s'" % (bright + 1, bright + 2, name))
    db.commit()
    cursor.close()

def insert_node_into(parent_name, name):
    cursor = db.cursor()
    cursor.execute("SELECT nsleft FROM nstree WHERE value = '%s' " % (str(parent_name),))
    rows = cursor.fetchone()
 
    bleft = rows[0] 

    cursor.execute("UPDATE nstree SET nsright = nsright + 2 WHERE nsright > " + str(bleft))
    cursor.execute("UPDATE nstree SET nsleft = nsleft + 2 WHERE nsleft > " + str(bleft))

    cursor.execute("INSERT INTO nstree SET nsleft = %d, nsright = %d, value = '%s'" % (bleft + 1, bleft + 2, name))
    db.commit()
    cursor.close()


# Populate Tree
insert_node_next_to(None, "Superhero")
insert_node_into("Superhero", "Duck")
insert_node_into("Superhero", "Japanese")
insert_node_into("Superhero", "Chinese")
insert_node_into("Chinese", "Jack Shen")
insert_node_into("Chinese", "Chinaman")
insert_node_into("Chinaman", "Nathan Hsiao")
insert_node_into("Chinaman", "Ming")
insert_node_into("Duck", "Silp Udom")
insert_node_into("Duck", "What the duck")
insert_node_into("Japanese", "Gozilla")

print get_tree()	

db.close()