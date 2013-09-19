#!/usr/bin/php
<?php
/**
 * bcrypt.php
 *
 * OK, so, I looked at python's implementation of bcrypt, and I thought to myself: "Self, cryptography is hard. Sure,
 * I could take some time and learn how to properly use Python's encryption stuff in multiple, complex lines of stuff,
 * or I could encrypt this in one line of PHP.
 * Then the guy on my other shoulder with the halo popped up and said: "This is PHP. You know what they say about using
 * PHP without understanding what you're doing."
 * "But self, It's sooo easy. Look, it's just one function. All the hard stuff is hidden from me."
 * "Remember when SQL was 'so easy' to implement, and then we saw all of the $_GET directly in the query?"
 *
 * Then I compromised. I will offload this to the easy, but ill-reputed PHP for right now, just to get the project done.
 * Then I will come back later and teach myself about Python's encryption over-complexity.
 *
 * And so, you have this script handling the encryption.
 *
 * args:
 * 1= option
 *  -e for encrypt
 *  -v for verify
 * 2= string for encrypt
 * 3= string for hash verification
 *
 *
 *
 */
$version=explode('.',phpversion());
$compiled_vers=$version[0]*10+$version[1];
if ($compiled_vers<55)
{
    exit("-1");
}

// test
//print_r($argv);

if($argv[1]=="-e") {
    $options=array('cost'=>11);
    echo password_hash($argv[2], PASSWORD_BCRYPT,$options);
}

else if($argv[1]=="-v") {

    if(password_verify($argv[2],$argv[3])) {
        exit("1");
    }

    else {
        exit("0");
    }
}


