# Makefile for gjko plugin plugin 
UI_FILES = $(wildcard dialogs/Ui_*.ui)
UI_FILESPY = $(addprefix dialogs/,$(notdir $(UI_FILES:.ui=.py))) 
PYC_FILES = $(wildcard */*.pyc) $(wildcard *.pyc)

RESOURCE_FILES = resources.py

default: compile
	
compile: $(UI_FILESPY) $(RESOURCE_FILES)

%.py: %.qrc
	pyrcc4-2.7 -o $@  $<

%.py: %.ui
	pyuic4-2.7 -o $@ $<

clean:
	rm -f $(PYC_FILES)
	rm -f $(UI_FILESPY)

package: clean compile
	zip ../release.zip -r ../gjko-plugin
