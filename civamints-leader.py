#!/usr/bin/python

# This shitshow is matt's fault, so it's all copyrighted and stuff by him:
# copyright 2012: matthew j weaver
# you can do whatever the fuck you please with this file as long as you keep
# this notice intact:
#
#   #####    ###   #     #    #    #     #   ###   #     # #######  #####
#  #     #    #    #     #   # #   ##   ##    #    ##    #    #    #     #
#  #          #    #     #  #   #  # # # #    #    # #   #    #    #
#  #          #    #     # #     # #  #  #    #    #  #  #    #     #####
#  #          #     #   #  ####### #     #    #    #   # #    #          #
#  #     #    #      # #   #     # #     #    #    #    ##    #    #     #
#   #####    ###      #    #     # #     #   ###   #     #    #     #####


import os
import os.path
import re
import sys

k_civamints_dir = "/Users/seant/Dropbox/Civ PBEM/IB 20120222"
k_savegame_pattern = "IB_20120222_[^.]*[.]CivBeyondSwordSave"
k_savegame_re = re.compile(k_savegame_pattern)
k_stupid_human = """
  Look, I'm not the smart one in the room.
  That's your job. Get it together.
"""
##k_sucka_mcs should be in order
k_sucka_mcs = [ "Giles", "JWM", "MJW", "Rory", "seant" ]
k_valid_mc_pairs = (("Rory", "MJW"), ("MJW", "JWM"), ("JWM", "Giles"),
                    ("Giles", "seant"), ("seant", "Rory"))


# Exceptions are for the weak. BLAME(matt)
def OhGodNow(error):
  print k_stupid_human
  print error
  sys.exit(1)

def IsSaveGame(filename):
  return k_savegame_re.match(filename)

# Oh, yeah. A player named, like, "CivBeyondSword" completely fucks this
# half-assed implementation.
def DiscoverMC(filename):
  for mc in k_sucka_mcs:
    if re.match(".*%s.*" % mc, filename):
      break
  return mc

# Compares filenames by mtime.
def CompareSavegames(a, b):
  a_mtime = os.stat(os.path.join(k_civamints_dir,a)).st_mtime
  b_mtime = os.stat(os.path.join(k_civamints_dir,b)).st_mtime
  return int(round(a_mtime - b_mtime))
  
def GetSortedSavegames():
  savegames = filter(IsSaveGame, os.listdir(k_civamints_dir))
  # We're completely dependent below on the savegames sorting in reverse
  # chronilogical order.
  return sorted(savegames, CompareSavegames)

# savegames MUST be sorted in reverse chronological order.
# returns a list of (mtime, player) tuples.
def GetSaveTimes(savegames):
  save_times = []
  for game in savegames:
    stat = os.stat(os.path.join(k_civamints_dir,game))
    save_times.append((stat.st_mtime, DiscoverMC(game)))
  return save_times

# Returns (shame_by_mc, (best, mc), (worst, mc))
def GetShameByMC(save_times):
  shame_by_mc = {}
  worst = 0
  best = 100000000000000000
  #print save_times
  for i in range(0, len(save_times) - 1):
    newer_time = save_times[i+1][0]
    older_time = save_times[i][0]
    # MC in PRIOR game gets credit. as in: MJW gets credit for time until JWM
    # savegame.
    mc = save_times[i][1]
    next_mc = save_times[i+1][1]
    shame = newer_time - older_time
    #print shame
    if shame < 0:
      #print "OH GOD! invalid shame: %s %d" % (mc, shame)
      continue
    if not (mc, next_mc) in k_valid_mc_pairs:
      #print "OH GOD! Missing save game? %s -> %s" % (mc, next_mc)
      continue
    if not mc in shame_by_mc:
      shame_by_mc[mc] = []
    shame_by_mc[mc].append(shame/60)
    if shame >= worst:
      worst = shame
      worst_mc = mc
    if shame <= best:
      best = shame
      best_mc = mc
  print "  Most Shameful Time: %d minutes (WAY TO GO, %s)" % (worst/60, worst_mc)
  print "  Least Shameful Time: %d SECONDS (WAY TO GO, %s)" % (best, best_mc)
  return shame_by_mc

# returns dictionary keyed by average shame in seconds, with values of the
# shamed MC. this makes it easy for a lazy person like me to rank the results by
# sorting the keys.
def GetAverageShame(shame_by_mc):
  avg_shame = {}
  for mc in shame_by_mc.keys():
    avg = sum(shame_by_mc[mc]) / len(shame_by_mc[mc])
    avg_shame[avg] = mc
  return avg_shame

# Standard disclaimers apply: savegames need to be sorted chronologically.
def ShameMCs(savegames):
  shame_by_mc = GetShameByMC(GetSaveTimes(savegames))
  avg_shame = GetAverageShame(shame_by_mc)
  print "  Average shameful times:"
  for k in sorted(avg_shame.keys(), reverse = True):
    print "    %s : %f minutes" % (avg_shame[k], k)


if __name__ == "__main__":
  try:
    if not os.path.exists(k_civamints_dir):
      OhGodNow("%s doesn't exist." % (k_civamints_dir))
    print "BEHOLD YOUR SHAME!"
    savegames = GetSortedSavegames()
    print "\nLast Round:"
    theLastRound=savegames[-(len(k_sucka_mcs)*2):]
    theStart=""
    theEnd=""
    for aFile in (theLastRound):
        ##even though the file says 'seant' it was saved by Giles
        if "seant" in (aFile):
            if theStart=="":
                theStart=theLastRound.index(aFile)
            else:
                theEnd=theLastRound.index(aFile)+1
                break
    ###shorten the list so it is just seant to seant
    theLastRound=theLastRound[theStart:theEnd]
    #print theLastRound   
    ShameMCs(theLastRound)
    
    ###I am not convinced the following is correct
    print "\nLast Ten Rounds:"
    ShameMCs(savegames[0:(len(k_sucka_mcs)*10)])
    
    print "\nAll Time:"
    ShameMCs(savegames)
    
    print "\nSpecial Shame Mention:\n  seant for making repeated mistakes when he was 'fixing' the code for this."
    
  except Exception:
    OhGodNow("OMFG EXCEPTION: %s" % Exception)
