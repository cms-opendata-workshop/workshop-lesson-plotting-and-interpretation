---
title: "Introduction"
teaching: 0
exercises: 0
questions:
- "How do I make plots of the skimmed datasets?"
- "How do I setup my ROOT environment?"
objectives:
- "Set up a ROOT environment that works for you"
- "Launch ROOT to test the setup"
- "Quickly browse the contents of a ROOT file with TBrowser"
keypoints:
- "The most straightforward way to open your skimmed files is with ROOT"
- "There are different plotting libraries out there but you can get started pretty easily with ROOT"
---

So you've skimmed some data and you want to start looking at it. Great! Since
these are most likely ROOT files, it's worth starting with ROOT to inspect them 
and make some plots. There are other standalone tools like [uproot](https://github.com/scikit-hep/uproot)
that allow you to interact with these files, but we'll stick with ROOT for this exercise. 

## Setting up a ROOT environment

Ideally, prior to starting this exercise, you will have gone through 
the [ROOT pre-exercise](https://cms-opendata-workshop.github.io/workshop-lesson-root/).
If you haven't gone through the full tutorial, that's OK, but you should 
definitely have gone through the module that shows you how to 
[setup a working ROOT environment](https://cms-opendata-workshop.github.io/workshop-lesson-root/02-get-root/index.html).

> ## Workflow for this lesson
> We have found that there are sometimes issues with X11 forwarding and getting
> windows and GUIs to pop up when the applications are launched from within
> docker or a VM. That's OK! 
>
> In this lesson, you can choose to view the plots one of two different ways:
> * If X11 forwarding works, you will see some of the plots pop up. 
> * Otherwise, the scripts we'll be using will produce `.png` images which you can 
> copy to your local machine for viewing. 
> 
> It's up to you which approach you want to use. 
>
> You *will* need to edit the files though, so whichever workflow you use, make sure
> you have an editor you are comfortable with. 
{: .callout}

### Docker-specific commands for X11 forwarding and other miscellany

If you want to use same ROOT-installed docker container as the 
[pre-exercises](https://cms-opendata-workshop.github.io/workshop-lesson-root/) and want to have X11
forwarding *and* a named container so you can come back to it, you can run the following command:

~~~
docker run --name root6 --net=host --env="DISPLAY" --volume="$HOME/.Xauthority:/home/cmsusr/.Xauthority:rw" -it rootproject/root:6.22.02-conda /bin/bash
~~~
{: .language-bash}

If you're running the above for the first time, it may take ~10 minutes to download the Docker files. 

Afterwards, you can alway restart the container with 

~~~
docker start -i root6
~~~
{: .language-bash}

Note that when the container starts up, you are in the '/' directory. You will want to 
get to the home directory
`/root` by typing

~~~
cd
~~~
{: .language-bash}

You should make sure there is an editor you feel comfortable with. You can install
new packages with `apt`. For example, to install `vim` or `nano` you would run one of
the following from inside the docker container. 

~~~
apt install vim
apt install nano
~~~
{: .language-bash}


### VM-specific commands go here

Looking forward to some feedback from the participants! :)


## Download the files and code we'll use

We are going to be running through parts of the open data analysis,
[Analysis of Higgs boson decays to two tau leptons using data and simulation of events at the CMS detector from 2012](http://opendata.cern.ch/record/12350),
which some of you may have done as part of the pre-exercises. 

> ## Analysis description
> *This analysis uses data and simulation of events at the CMS experiment from 
> 2012 with the goal to study decays of a Higgs boson into two tau leptons 
> in the final state of a muon lepton and a hadronically decayed tau lepton. 
> The analysis follows loosely the setup of the official CMS analysis published in 2014.*
{: .callout}

We'll be looking at the skimmed ROOT files, but those files can take considerable time to 
generate, depending on where you are and your internet connection. To save time, we've run
**Step 1** of that exercise already and generated the skimmed ROOT files. We've also 
modified some of the scripts slightly to make it easier to copy the files out of the VM/container
and included some new, simpler files that allow you to inspect these ROOT files
and make some first-order plots. 

If you haven't yet, you may want to check out the [analysis](http://opendata.cern.ch/record/12350)
to get a feel for the physics. 



{% include links.md %}

