CFLAGS += $(shell python3-config --cflags)
LDFLAGS += $(shell python3-config --ldflags)

compile:
	gcc $(CFLAGS) -fPIC -c test_capi.c -o test_capi.o
	gcc test_capi.o -Xlinker -export-dynamic  $(LDFLAGS) -lpython3.8 -o test_capi.out

run: compile
	./test_capi.out

clean:
	rm -rf test_capi.o
	rm -rf test_capi.out

.phony:
	clean
