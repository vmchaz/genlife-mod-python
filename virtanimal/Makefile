CC = gcc
LINK = $(CC)
STRIP = strip

SRC = ./src
BUILD = ./objs
LIB = ./lib

CFLAGS      = -g -O2 $$(python3-config --includes --ldflags) -Wincompatible-pointer-types
CSAHREDLIBS = -shared

INCS = -I$(SRC) 

DEPS = $(SRC)/test.h

OBJS = $(BUILD)/test.o \
	$(BUILD)/animal.o \
	$(BUILD)/animal_repr.o \
	$(BUILD)/vcpu.o \
	$(BUILD)/vcpu_repr.o \
	$(BUILD)/unitvarstruct.o \
	$(BUILD)/unitvarstruct_repr.o \
	$(BUILD)/fieldpart.o \
	$(BUILD)/fieldpart_repr.o \
	$(BUILD)/instructionsequence.o \
	$(BUILD)/instructionsequence_repr.o \
	$(BUILD)/callbackinfo.o \
	$(BUILD)/advanced_func.o

BINS = $(BUILD)/virtanimal.so

BINS2 = virtanimal.so 

all: prebuild \
	$(BINS)

$(BUILD)/virtanimal.so: \
	$(OBJS)
	$(CC) $(CFLAGS) $(CSAHREDLIBS) -o $(LIB)/virtanimal.so $(OBJS)
	$(STRIP) --strip-unneeded $(LIB)/virtanimal.so

$(BUILD)/test.o: $(DEPS) \
	$(SRC)/test.c
	$(CC) -c $(CFLAGS) -fPIC $(INCS) -o $(BUILD)/test.o $(SRC)/test.c
	
	
$(BUILD)/animal.o: $(DEPS) \
	$(SRC)/animal.c
	$(CC) -c $(CFLAGS) -fPIC $(INCS) -o $(BUILD)/animal.o $(SRC)/animal.c
	
$(BUILD)/animal_repr.o: $(DEPS) \
	$(SRC)/animal_repr.c
	$(CC) -c $(CFLAGS) -fPIC $(INCS) -o $(BUILD)/animal_repr.o $(SRC)/animal_repr.c
	
$(BUILD)/vcpu.o: $(DEPS) \
	$(SRC)/vcpu.c
	$(CC) -c $(CFLAGS) -fPIC $(INCS) -o $(BUILD)/vcpu.o $(SRC)/vcpu.c
	
$(BUILD)/vcpu_repr.o: $(DEPS) \
	$(SRC)/vcpu_repr.c
	$(CC) -c $(CFLAGS) -fPIC $(INCS) -o $(BUILD)/vcpu_repr.o $(SRC)/vcpu_repr.c
	
$(BUILD)/unitvarstruct.o: $(DEPS) \
	$(SRC)/unitvarstruct.c
	$(CC) -c $(CFLAGS) -fPIC $(INCS) -o $(BUILD)/unitvarstruct.o $(SRC)/unitvarstruct.c
	
$(BUILD)/unitvarstruct_repr.o: $(DEPS) \
	$(SRC)/unitvarstruct_repr.c
	$(CC) -c $(CFLAGS) -fPIC $(INCS) -o $(BUILD)/unitvarstruct_repr.o $(SRC)/unitvarstruct_repr.c
	
$(BUILD)/fieldpart.o: $(DEPS) \
	$(SRC)/fieldpart.c
	$(CC) -c $(CFLAGS) -fPIC $(INCS) -o $(BUILD)/fieldpart.o $(SRC)/fieldpart.c
	
$(BUILD)/fieldpart_repr.o: $(DEPS) \
	$(SRC)/fieldpart_repr.c
	$(CC) -c $(CFLAGS) -fPIC $(INCS) -o $(BUILD)/fieldpart_repr.o $(SRC)/fieldpart_repr.c
	
$(BUILD)/instructionsequence.o: $(DEPS) \
	$(SRC)/instructionsequence.c
	$(CC) -c $(CFLAGS) -fPIC $(INCS) -o $(BUILD)/instructionsequence.o $(SRC)/instructionsequence.c
	
$(BUILD)/instructionsequence_repr.o: $(DEPS) \
	$(SRC)/instructionsequence_repr.c
	$(CC) -c $(CFLAGS) -fPIC $(INCS) -o $(BUILD)/instructionsequence_repr.o $(SRC)/instructionsequence_repr.c
	
$(BUILD)/callbackinfo.o: $(DEPS) \
	$(SRC)/callbackinfo.c
	$(CC) -c $(CFLAGS) -fPIC $(INCS) -o $(BUILD)/callbackinfo.o $(SRC)/callbackinfo.c
	
$(BUILD)/advanced_func.o: $(DEPS) \
	$(SRC)/advanced_func.c
	$(CC) -c $(CFLAGS) -fPIC $(INCS) -o $(BUILD)/advanced_func.o $(SRC)/advanced_func.c

clean:
	rm -rf $(BUILD)
	rm -rf $(LIB)

prebuild:
	test -d $(BUILD) || mkdir -p $(BUILD)
	test -d $(LIB) || mkdir -p $(LIB)
	
install: 
	ldconfig
