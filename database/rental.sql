-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 19, 2025 at 05:30 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 7.3.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rental`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `username`, `password`, `email`) VALUES
(7, 'bayu', '12345', ''),
(8, 'dodo', 'bayu', '');

-- --------------------------------------------------------

--
-- Table structure for table `karyawan`
--

CREATE TABLE `karyawan` (
  `id_karyawan` int(11) NOT NULL,
  `nama_karyawan` varchar(50) NOT NULL,
  `alamat` varchar(50) NOT NULL,
  `no_telp` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `karyawan`
--

INSERT INTO `karyawan` (`id_karyawan`, `nama_karyawan`, `alamat`, `no_telp`) VALUES
(1, 'Bayu Aji Utomo', 'Surakarta', '081225604346'),
(2, 'Riko Ferdiansyah', 'Surakarta', '085724539865'),
(3, 'Soffin Thoriq', 'Surakarta', '085699538765'),
(4, 'Galih Muhammad', 'Surakarta', '083821515526');

-- --------------------------------------------------------

--
-- Table structure for table `mobil`
--

CREATE TABLE `mobil` (
  `id_mobil` int(11) NOT NULL,
  `merek` varchar(50) NOT NULL,
  `warna` varchar(50) NOT NULL,
  `no_plat` varchar(50) NOT NULL,
  `harga_sewa` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `mobil`
--

INSERT INTO `mobil` (`id_mobil`, `merek`, `warna`, `no_plat`, `harga_sewa`) VALUES
(11, 'Lamborgini', 'Merah', 'AD 6979 PO', '12.000.000'),
(12, 'Lamborgini', 'Putih', 'AD 911 PR', '10.000.000'),
(21, 'Ferarri', 'Hitam', 'AD 6574 PK', '8.000.000'),
(22, 'Ferarri', 'Abu-abu', 'AD 7732 PL', '8.500.000'),
(23, 'Bugatti', 'Putih', 'AD 4200 BK', '15.000.000'),
(31, 'Porche', 'Putih', 'AD 7489 PE', '13.000.000'),
(32, 'Porche', 'Abu-abu', 'AD 9987 PR', '12.600.000'),
(41, 'Koenigseg', 'Hitam', 'AD 6996 PP', '10.000.000'),
(42, 'Koenigseg', 'Abu-abu', 'AD 741 LO', '11.000.000'),
(51, 'Corvette', 'Putih', 'AD 8481 KW', '25.000.000'),
(52, 'Ferarri', 'Hitam', 'AD 8957 LU', '20.000.000'),
(53, 'Porche', 'Merah', 'AD 9081 OK', '8.000.000'),
(61, 'Porche', 'Putih', 'AD 5647 JK', '14.000.000'),
(100, 'Lamborgini', 'Hitam', 'AD 123 RY', '12.000.000');

-- --------------------------------------------------------

--
-- Table structure for table `pelanggan`
--

CREATE TABLE `pelanggan` (
  `id_pelanggan` int(11) NOT NULL,
  `nama_pelanggan` varchar(50) NOT NULL,
  `alamat` varchar(50) NOT NULL,
  `jenis_kelamin` varchar(50) NOT NULL,
  `no_telp` varchar(50) NOT NULL,
  `mobil` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pelanggan`
--

INSERT INTO `pelanggan` (`id_pelanggan`, `nama_pelanggan`, `alamat`, `jenis_kelamin`, `no_telp`, `mobil`) VALUES
(1, 'Sumarni', 'solo', 'Perempuan', '089667899087', 'Lamborgini'),
(2, 'Suraji', 'Mojosongo', 'Laki-laki', '085724539865', 'Ferarri'),
(3, 'Sumanto', 'Sragen', 'Laki-laki', '086846730987', 'Porche'),
(4, 'Pratman', 'Surakarta', 'Laki-laki', '089614089089', 'Bugatti'),
(5, 'Walidi', 'Sukoharjo', 'Laki-laki', '085724539865', 'Porche'),
(20, 'Ronaldo', 'Boyolali', 'Laki-laki', '089614089089', 'Ferarri');

-- --------------------------------------------------------

--
-- Table structure for table `sewa`
--

CREATE TABLE `sewa` (
  `id_sewa` int(11) NOT NULL,
  `id_mobil` int(11) NOT NULL,
  `tgl_sewa` date NOT NULL,
  `tgl_kembali` date NOT NULL,
  `total_bayar` varchar(50) NOT NULL,
  `denda` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sewa`
--

INSERT INTO `sewa` (`id_sewa`, `id_mobil`, `tgl_sewa`, `tgl_kembali`, `total_bayar`, `denda`) VALUES
(1, 11, '2025-02-17', '2025-02-18', '12.000.000', '-'),
(2, 23, '2025-01-09', '2025-01-10', '15.000.000', '-'),
(3, 21, '2025-02-09', '2025-02-10', '8.000.000', '-'),
(4, 31, '2025-02-17', '2025-02-18', '13.000.000', '-');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `karyawan`
--
ALTER TABLE `karyawan`
  ADD PRIMARY KEY (`id_karyawan`);

--
-- Indexes for table `mobil`
--
ALTER TABLE `mobil`
  ADD PRIMARY KEY (`id_mobil`);

--
-- Indexes for table `pelanggan`
--
ALTER TABLE `pelanggan`
  ADD PRIMARY KEY (`id_pelanggan`);

--
-- Indexes for table `sewa`
--
ALTER TABLE `sewa`
  ADD PRIMARY KEY (`id_sewa`,`id_mobil`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `karyawan`
--
ALTER TABLE `karyawan`
  MODIFY `id_karyawan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `mobil`
--
ALTER TABLE `mobil`
  MODIFY `id_mobil` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=112;

--
-- AUTO_INCREMENT for table `pelanggan`
--
ALTER TABLE `pelanggan`
  MODIFY `id_pelanggan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `sewa`
--
ALTER TABLE `sewa`
  MODIFY `id_sewa` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
