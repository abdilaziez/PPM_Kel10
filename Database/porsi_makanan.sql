-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 12 Jun 2021 pada 15.08
-- Versi server: 10.4.16-MariaDB
-- Versi PHP: 7.4.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `porsi_makanan`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `akun_admin`
--

CREATE TABLE `akun_admin` (
  `ID_akun` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `akun_admin`
--

INSERT INTO `akun_admin` (`ID_akun`, `username`, `password`) VALUES
(1, 'admin', 'admin');

-- --------------------------------------------------------

--
-- Struktur dari tabel `jenis_makanan`
--

CREATE TABLE `jenis_makanan` (
  `ID_jenis_makanan` int(11) NOT NULL,
  `nama_jenis_makanan` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `jenis_makanan`
--

INSERT INTO `jenis_makanan` (`ID_jenis_makanan`, `nama_jenis_makanan`) VALUES
(1, 'Buah');

-- --------------------------------------------------------

--
-- Struktur dari tabel `makanan`
--

CREATE TABLE `makanan` (
  `ID_makanan` int(11) NOT NULL,
  `nama_makanan` varchar(255) NOT NULL,
  `tipe_makanan` int(11) NOT NULL,
  `massa_dewasa` varchar(10) NOT NULL,
  `massa_bayi` varchar(10) NOT NULL,
  `massa_anak_4_10_tahun` varchar(10) NOT NULL,
  `massa_anak_11_18_tahun` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `makanan`
--

INSERT INTO `makanan` (`ID_makanan`, `nama_makanan`, `tipe_makanan`, `massa_dewasa`, `massa_bayi`, `massa_anak_4_10_tahun`, `massa_anak_11_18_tahun`) VALUES
(1, 'Apel (tidak dikupas)', 1, '150gr', 'Dilarang', '87,5gr', '125gr'),
(2, 'Aprikot (kering)', 1, '30gr', 'Dilarang', '22,5gr', '27,5gr'),
(3, 'Aprikot (Segar)', 1, '100gr', 'Dilarang', '75gr', '90gr'),
(4, 'Pisang (Tidak dikupas)', 1, '150gr', 'Dilarang', '87,5gr', '125gr'),
(5, 'Blueberry', 1, '80gr', 'Dilarang', '50gr', '80gr');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `akun_admin`
--
ALTER TABLE `akun_admin`
  ADD PRIMARY KEY (`ID_akun`);

--
-- Indeks untuk tabel `jenis_makanan`
--
ALTER TABLE `jenis_makanan`
  ADD PRIMARY KEY (`ID_jenis_makanan`);

--
-- Indeks untuk tabel `makanan`
--
ALTER TABLE `makanan`
  ADD PRIMARY KEY (`ID_makanan`),
  ADD KEY `nama_makananXjenis_makanan` (`tipe_makanan`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `akun_admin`
--
ALTER TABLE `akun_admin`
  MODIFY `ID_akun` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT untuk tabel `jenis_makanan`
--
ALTER TABLE `jenis_makanan`
  MODIFY `ID_jenis_makanan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT untuk tabel `makanan`
--
ALTER TABLE `makanan`
  MODIFY `ID_makanan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `makanan`
--
ALTER TABLE `makanan`
  ADD CONSTRAINT `nama_makananXjenis_makanan` FOREIGN KEY (`tipe_makanan`) REFERENCES `jenis_makanan` (`ID_jenis_makanan`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
