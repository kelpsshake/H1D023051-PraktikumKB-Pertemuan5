% JURUSANKU
% Program sistem pakar untuk menentukan jurusan kuliah berdasarkan minat

% DATABASE DINAMIS
:- dynamic minat_pos/1.
:- dynamic minat_neg/1.

% FAKTA JURUSAN
jurusan("Informatika").
jurusan("Desain Komunikasi Visual").
jurusan("Psikologi").
jurusan("Teknik Mesin").
jurusan("Ilmu Komunikasi").

% HUBUNGAN MINAT DENGAN JURUSAN
minat(suka_komputer, "Informatika").
minat(logika_kuat, "Informatika").
minat(suka_menganalisis, "Informatika").

minat(suka_menggambar, "Desain Komunikasi Visual").
minat(kreatif, "Desain Komunikasi Visual").
minat(suka_mengedit_video, "Desain Komunikasi Visual").

minat(suka_membaca, "Psikologi").
minat(suka_mendengar, "Psikologi").
minat(suka_mempelajari_manusia, "Psikologi").

minat(suka_praktik, "Teknik Mesin").
minat(suka_matematika, "Teknik Mesin").

minat(suka_berdiskusi, "Ilmu Komunikasi").
minat(suka_bicara, "Ilmu Komunikasi").
minat(suka_bekerja_dalam_tim, "Ilmu Komunikasi").
minat(suka_menulis, "Ilmu Komunikasi").

% PERTANYAAN
pertanyaan(suka_komputer, Q) :-
    Q = "Apakah kamu suka menggunakan atau bermain dengan komputer?".

pertanyaan(logika_kuat, Q) :-
    Q = "Apakah kamu merasa punya logika yang kuat dalam menyelesaikan masalah?".

pertanyaan(suka_menganalisis, Q) :-
    Q = "Apakah kamu suka menganalisis suatu masalah secara mendalam?".

pertanyaan(suka_menggambar, Q) :-
    Q = "Apakah kamu suka menggambar atau membuat ilustrasi?".

pertanyaan(kreatif, Q) :-
    Q = "Apakah kamu merasa kamu adalah orang yang kreatif?".

pertanyaan(suka_mengedit_video, Q) :-
    Q = "Apakah kamu suka mengedit video atau membuat konten visual?".

pertanyaan(suka_membaca, Q) :-
    Q = "Apakah kamu suka membaca buku atau artikel?".

pertanyaan(suka_mendengar, Q) :-
    Q = "Apakah kamu suka mendengarkan cerita atau curhatan orang lain?".

pertanyaan(suka_mempelajari_manusia, Q) :-
    Q = "Apakah kamu tertarik mempelajari perilaku dan pikiran manusia?".

pertanyaan(suka_praktik, Q) :-
    Q = "Apakah kamu lebih suka praktik langsung daripada teori?".

pertanyaan(suka_matematika, Q) :-
    Q = "Apakah kamu menyukai pelajaran matematika atau fisika?".

pertanyaan(suka_berdiskusi, Q) :-
    Q = "Apakah kamu suka berdiskusi atau debat?".

pertanyaan(suka_bicara, Q) :-
    Q = "Apakah kamu suka berbicara di depan umum?".

pertanyaan(suka_bekerja_dalam_tim, Q) :-
    Q = "Apakah kamu suka bekerja sama dalam kelompok atau tim?".

pertanyaan(suka_menulis, Q) :-
    Q = "Apakah kamu suka menulis cerita, artikel, atau jurnal?".