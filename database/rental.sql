-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 18, 2024 at 05:57 AM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

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
(1, 'ersiaditya', 'aditya88', 'ersiaditya@gmail.com'),
(2, 'syafiqvalent', 'valent1945', ''),
(4, 'wahyu', 'Duraamira11', ''),
(5, 'wahyu123', 'wahyu321', ''),
(6, 'ersiaditya96', 'aditya88', '');

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
(1, 'Ersi Aditya', 'Gabek 2', '089610069069'),
(2, 'Wahyu', 'Bukit Merapin', '085724539865'),
(3, 'Syafiq Valent', 'Toboali', '085699538765'),
(4, 'Fauzan Ar Muzadi', 'Toboali', '087790875382');

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
(11, 'Creta', 'Merah', 'BN 6979 PO', '200.000'),
(12, 'Creta', 'Putih', 'BN 911 PR', '200.000'),
(21, 'Palisade', 'Hitam', 'BN 6574 PK', '250.000'),
(22, 'Palisade', 'Abu-abu', 'BN 7732 PL', '250.000'),
(23, 'Palisade', 'Putih', 'BN 4200 BK', '250.000'),
(31, 'Santa FE', 'Putih', 'BN 7489 PE', '220.000'),
(32, 'Santa FE', 'Abu-abu', 'BN 9987 PR', '220.000'),
(41, 'IONIQ 6', 'Hitam', 'BN 6996 PP', '240.000'),
(42, 'IONIQ 6', 'Abu-abu', 'BN 741 LO', '240.000'),
(51, 'Stargazer', 'Putih', 'BN 8481 KW', '235.000'),
(52, 'Stargazer', 'Hitam', 'BN 8957 LU', '235.000'),
(53, 'Stargazer', 'Merah', 'BN 9081 OK', '235.000'),
(61, 'Stargazer X', 'Putih', 'BN 5647 JK', '250.000');

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
(1, 'Rois', 'Selindung Baru', 'Laki-laki', '089667899087', 'Santa FE'),
(2, 'Rakha', 'Pintu Air', 'Laki-laki', '085724539865', 'Palisade'),
(3, 'Syafiq', 'Toboali', 'Laki-laki', '086846730987', 'Santa FE'),
(4, 'Wahyu', 'Gabek', 'Laki-laki', '089614089089', 'Creta'),
(5, 'Aldo', 'Toboali', 'Laki-laki', '085724539865', 'IONIQ 6'),
(20, 'Ersi', 'Gabek 2', 'Laki-laki', '089614089089', 'IONIQ 6');

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
(1, 11, '2024-01-07', '2024-01-16', '400.000', '-'),
(2, 23, '2024-01-02', '2024-01-03', '250.000', '-'),
(3, 21, '2024-01-01', '2024-01-02', '400.000', '-'),
(4, 31, '2024-01-15', '2024-01-16', '200.000', '-');

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `karyawan`
--
ALTER TABLE `karyawan`
  MODIFY `id_karyawan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `mobil`
--
ALTER TABLE `mobil`
  MODIFY `id_mobil` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=63;

--
-- AUTO_INCREMENT for table `pelanggan`
--
ALTER TABLE `pelanggan`
  MODIFY `id_pelanggan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `sewa`
--
ALTER TABLE `sewa`
  MODIFY `id_sewa` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
