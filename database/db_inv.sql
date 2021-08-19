-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 18 Agu 2021 pada 19.24
-- Versi server: 10.4.6-MariaDB
-- Versi PHP: 7.3.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_inv`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `authtoken_token`
--

CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `authtoken_token`
--

INSERT INTO `authtoken_token` (`key`, `created`, `user_id`) VALUES
('2ac7e39d54b91de3ddc5f8822d5d0923abb5b5dc', '2021-08-18 06:13:16.023335', 1),
('b3d019235b9bd553b77c216cce936b3a6ce5934a', '2021-08-18 17:14:00.949326', 4);

-- --------------------------------------------------------

--
-- Struktur dari tabel `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(1, 'Admin'),
(4, 'petugas'),
(3, 'petugas baru');

-- --------------------------------------------------------

--
-- Struktur dari tabel `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktur dari tabel `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add petugas', 7, 'add_petugas'),
(26, 'Can change petugas', 7, 'change_petugas'),
(27, 'Can delete petugas', 7, 'delete_petugas'),
(28, 'Can view petugas', 7, 'view_petugas'),
(29, 'Can add pimpinan', 8, 'add_pimpinan'),
(30, 'Can change pimpinan', 8, 'change_pimpinan'),
(31, 'Can delete pimpinan', 8, 'delete_pimpinan'),
(32, 'Can view pimpinan', 8, 'view_pimpinan'),
(33, 'Can add ruangan', 9, 'add_ruangan'),
(34, 'Can change ruangan', 9, 'change_ruangan'),
(35, 'Can delete ruangan', 9, 'delete_ruangan'),
(36, 'Can view ruangan', 9, 'view_ruangan'),
(37, 'Can add barang', 10, 'add_barang'),
(38, 'Can change barang', 10, 'change_barang'),
(39, 'Can delete barang', 10, 'delete_barang'),
(40, 'Can view barang', 10, 'view_barang'),
(41, 'Can add cek barang', 11, 'add_cekbarang'),
(42, 'Can change cek barang', 11, 'change_cekbarang'),
(43, 'Can delete cek barang', 11, 'delete_cekbarang'),
(44, 'Can view cek barang', 11, 'view_cekbarang'),
(45, 'Can add pindah barang', 12, 'add_pindahbarang'),
(46, 'Can change pindah barang', 12, 'change_pindahbarang'),
(47, 'Can delete pindah barang', 12, 'delete_pindahbarang'),
(48, 'Can view pindah barang', 12, 'view_pindahbarang'),
(49, 'Can add inventaris', 13, 'add_inventaris'),
(50, 'Can change inventaris', 13, 'change_inventaris'),
(51, 'Can delete inventaris', 13, 'delete_inventaris'),
(52, 'Can view inventaris', 13, 'view_inventaris'),
(53, 'Can add Token', 14, 'add_token'),
(54, 'Can change Token', 14, 'change_token'),
(55, 'Can delete Token', 14, 'delete_token'),
(56, 'Can view Token', 14, 'view_token'),
(57, 'Can add token', 15, 'add_tokenproxy'),
(58, 'Can change token', 15, 'change_tokenproxy'),
(59, 'Can delete token', 15, 'delete_tokenproxy'),
(60, 'Can view token', 15, 'view_tokenproxy');

-- --------------------------------------------------------

--
-- Struktur dari tabel `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$260000$L5PHQh68d5iGDfvLrKG9Nw$Ot1diAKnMWUjSzBWXfAHOxBDh+SK5ko/RzabVrefW2o=', '2021-08-18 14:16:15.349451', 1, 'admin', '', '', 'admin@gmail.com', 1, 1, '2021-08-18 05:21:12.000000'),
(2, 'pbkdf2_sha256$260000$HQ4pZyNvtkguKfwU7OCJnu$FYay1O8xR94N8QSR9jwY03hV3xxjJTv3a5jUBlIJ5ZI=', NULL, 0, 'baru@gmail.com', '', '', '', 1, 0, '2021-08-18 05:35:59.000000'),
(3, 'pbkdf2_sha256$260000$eBSOieZOsJgrEdUQB0kvh2$fTPb2hToYuUJPFubkr7LEqtFQWZnVFJk1SaDn7LzeuU=', '2021-08-18 14:18:46.477043', 0, 'fida', '', '', 'fida@gmail.com', 1, 1, '2021-08-18 13:59:17.000000'),
(4, 'pbkdf2_sha256$260000$UgA3aDBBBqZrqOGGxlnbhh$wcUvGfqyWgLyr1YrUOf1YNmABp62Yu4kM1rqupmaV/U=', '2021-08-18 17:16:49.292293', 1, 'hasan', '', '', 'hasan@gmail.com', 1, 1, '2021-08-18 14:38:59.000000');

-- --------------------------------------------------------

--
-- Struktur dari tabel `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `auth_user_groups`
--

INSERT INTO `auth_user_groups` (`id`, `user_id`, `group_id`) VALUES
(3, 3, 3),
(4, 4, 4);

-- --------------------------------------------------------

--
-- Struktur dari tabel `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktur dari tabel `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL
) ;

--
-- Dumping data untuk tabel `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2021-08-18 05:32:09.452338', '1', 'hikmah', 1, '[{\"added\": {}}]', 7, 1),
(2, '2021-08-18 05:35:59.982475', '2', 'baru@gmail.com', 1, '[{\"added\": {}}]', 4, 1),
(3, '2021-08-18 05:36:22.903038', '2', 'baru@gmail.com', 2, '[{\"changed\": {\"fields\": [\"Staff status\"]}}]', 4, 1),
(4, '2021-08-18 05:54:41.666948', '1', 'Admin', 1, '[{\"added\": {}}]', 3, 1),
(5, '2021-08-18 05:58:25.225761', '1', 'admin', 2, '[]', 4, 1),
(6, '2021-08-18 06:12:11.785058', '1', 'admin', 2, '[]', 4, 1),
(7, '2021-08-18 10:52:37.256914', '2', 'Petugas', 1, '[{\"added\": {}}]', 3, 1),
(8, '2021-08-18 10:53:06.470225', '1', 'Admin', 2, '[]', 3, 1),
(9, '2021-08-18 10:53:24.394191', '2', 'baru@gmail.com', 2, '[]', 4, 1),
(10, '2021-08-18 12:47:26.169378', '2', 'hikmahlagi', 1, '[{\"added\": {}}]', 7, 1),
(11, '2021-08-18 13:51:06.654310', '1', 'Admin', 2, '[]', 3, 1),
(12, '2021-08-18 13:54:11.788704', '1', 'admin', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 4, 1),
(13, '2021-08-18 14:00:58.773613', '3', 'tanti', 1, '[{\"added\": {}}]', 7, 3),
(14, '2021-08-18 14:02:38.888122', '3', 'fida', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 4, 3),
(15, '2021-08-18 14:07:50.507474', '3', 'tanti', 2, '[]', 7, 3),
(16, '2021-08-18 14:09:35.967662', '2', 'Petugas', 2, '[{\"changed\": {\"fields\": [\"Permissions\"]}}]', 3, 3),
(17, '2021-08-18 14:11:47.252150', '3', 'fida', 2, '[{\"changed\": {\"fields\": [\"Superuser status\"]}}]', 4, 3),
(18, '2021-08-18 14:13:17.665749', '3', 'tanti', 2, '[{\"changed\": {\"fields\": [\"Status\"]}}]', 7, 3),
(19, '2021-08-18 14:14:24.908194', '2', 'Petugas', 2, '[{\"changed\": {\"fields\": [\"Permissions\"]}}]', 3, 3),
(20, '2021-08-18 14:15:33.940496', '3', 'fida', 2, '[]', 4, 1),
(21, '2021-08-18 14:15:46.761065', '2', 'Petugas', 2, '[]', 3, 1),
(22, '2021-08-18 14:16:49.605477', '3', 'petugas baru', 1, '[{\"added\": {}}]', 3, 1),
(23, '2021-08-18 14:17:06.696710', '3', 'tanti', 2, '[]', 7, 1),
(24, '2021-08-18 14:17:29.610419', '3', 'fida', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 4, 1),
(25, '2021-08-18 14:40:39.769538', '4', 'hasan', 2, '[]', 4, 4),
(26, '2021-08-18 14:40:55.134556', '2', 'Petugas', 3, '', 3, 4),
(27, '2021-08-18 14:41:07.801472', '4', 'petugas', 1, '[{\"added\": {}}]', 3, 4),
(28, '2021-08-18 14:41:23.869718', '4', 'hasan', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 4, 4),
(29, '2021-08-18 14:42:20.994473', '4', 'susan', 1, '[{\"added\": {}}]', 7, 4);

-- --------------------------------------------------------

--
-- Struktur dari tabel `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(14, 'authtoken', 'token'),
(15, 'authtoken', 'tokenproxy'),
(5, 'contenttypes', 'contenttype'),
(10, 'inventaris', 'barang'),
(11, 'inventaris', 'cekbarang'),
(13, 'inventaris', 'inventaris'),
(7, 'inventaris', 'petugas'),
(8, 'inventaris', 'pimpinan'),
(12, 'inventaris', 'pindahbarang'),
(9, 'inventaris', 'ruangan'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Struktur dari tabel `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-08-18 05:18:19.235150'),
(2, 'auth', '0001_initial', '2021-08-18 05:18:19.815922'),
(3, 'admin', '0001_initial', '2021-08-18 05:18:19.979114'),
(4, 'admin', '0002_logentry_remove_auto_add', '2021-08-18 05:18:20.007971'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2021-08-18 05:18:20.045950'),
(6, 'contenttypes', '0002_remove_content_type_name', '2021-08-18 05:18:20.158058'),
(7, 'auth', '0002_alter_permission_name_max_length', '2021-08-18 05:18:20.196219'),
(8, 'auth', '0003_alter_user_email_max_length', '2021-08-18 05:18:20.354019'),
(9, 'auth', '0004_alter_user_username_opts', '2021-08-18 05:18:20.380017'),
(10, 'auth', '0005_alter_user_last_login_null', '2021-08-18 05:18:20.458789'),
(11, 'auth', '0006_require_contenttypes_0002', '2021-08-18 05:18:20.466035'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2021-08-18 05:18:20.489381'),
(13, 'auth', '0008_alter_user_username_max_length', '2021-08-18 05:18:20.535160'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2021-08-18 05:18:20.571133'),
(15, 'auth', '0010_alter_group_name_max_length', '2021-08-18 05:18:20.616461'),
(16, 'auth', '0011_update_proxy_permissions', '2021-08-18 05:18:20.668971'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2021-08-18 05:18:20.705032'),
(18, 'authtoken', '0001_initial', '2021-08-18 05:18:20.824017'),
(19, 'authtoken', '0002_auto_20160226_1747', '2021-08-18 05:18:20.912745'),
(20, 'authtoken', '0003_tokenproxy', '2021-08-18 05:18:20.923739'),
(21, 'sessions', '0001_initial', '2021-08-18 05:18:20.982125'),
(22, 'inventaris', '0001_initial', '2021-08-18 05:19:50.893912'),
(23, 'inventaris', '0002_ruangan_user', '2021-08-18 08:35:56.171404'),
(24, 'inventaris', '0003_alter_ruangan_user', '2021-08-18 08:48:19.144201'),
(25, 'inventaris', '0004_alter_barang_lokasi_barang', '2021-08-18 09:15:19.011893'),
(26, 'inventaris', '0005_rename_lokasi_barang_barang_lokasi', '2021-08-18 10:40:18.432206'),
(27, 'inventaris', '0006_alter_barang_gambar', '2021-08-18 16:57:24.678865'),
(28, 'inventaris', '0007_delete_pimpinan', '2021-08-18 17:06:42.172113'),
(29, 'inventaris', '0008_auto_20210819_0011', '2021-08-18 17:12:05.311351');

-- --------------------------------------------------------

--
-- Struktur dari tabel `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('8mhkixixlzst9qw9rqvk4lafjpxqbusf', '.eJxVjEEOwiAQRe_C2hCmFKa4dN8zkAEGWzWQlHZlvLsh6UK3_73338LTsS_-aLz5NYmrAHH53QLFJ5cO0oPKvcpYy76tQXZFnrTJuSZ-3U7372ChtvTaIeCEpAhMzkmZEQZMLphokC0DIGilMSsOgwUXaKBsE4-KNU4ho_h8Ac9eN6E:1mGE8g:YcNcIguqGsHg2gPmvJayVzxAuRcARiGwN3mpvGqniHc', '2021-09-01 05:29:22.027364'),
('duvr2iyukuusr5qhoolfnbde5ns7dfus', '.eJxVjEEOwiAQRe_C2hCmFKa4dN8zkAEGWzWQlHZlvLsh6UK3_73338LTsS_-aLz5NYmrAHH53QLFJ5cO0oPKvcpYy76tQXZFnrTJuSZ-3U7372ChtvTaIeCEpAhMzkmZEQZMLphokC0DIGilMSsOgwUXaKBsE4-KNU4ho_h8Ac9eN6E:1mGG9E:zTO_ztvxjzMn-YXcoGg7k3c4eCI3hipidZk6wVMwfmo', '2021-09-01 07:38:04.229857'),
('r2usjqjlxu9490p1cnxdxhev7kzwcxa5', '.eJxVjDsOwjAQBe_iGln-O6GkzxmstdeLA8iW4qRC3J1ESgHtm5n3ZgG2tYSt5yXMyK7MsMvvFiE9cz0APqDeG0-trssc-aHwk3Y-Ncyv2-n-HRToZa8V6jQQGI3ordTkpXMyCiUH65W3FlOkUQMkQ24Ugmh3pRU-k1FGCWKfL9otN5s:1mGPBJ:c-a4HUT1bima2Frl61nHeFPvbyorXWSG7cMeZJLWhwU', '2021-09-01 17:16:49.299358');

-- --------------------------------------------------------

--
-- Struktur dari tabel `inventaris_barang`
--

CREATE TABLE `inventaris_barang` (
  `id` int(11) NOT NULL,
  `kode_barang` varchar(20) NOT NULL,
  `nama_barang` varchar(20) NOT NULL,
  `kondisi_barang` varchar(30) DEFAULT NULL,
  `jenis_barang` varchar(30) DEFAULT NULL,
  `kategori_barang` varchar(30) DEFAULT NULL,
  `tanggal` varchar(20) DEFAULT NULL,
  `tgl_update` varchar(20) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  `keterangan` varchar(50) DEFAULT NULL,
  `gambar` varchar(100) NOT NULL,
  `qrcode` varchar(100) NOT NULL,
  `lokasi_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `inventaris_barang`
--

INSERT INTO `inventaris_barang` (`id`, `kode_barang`, `nama_barang`, `kondisi_barang`, `jenis_barang`, `kategori_barang`, `tanggal`, `tgl_update`, `status`, `keterangan`, `gambar`, `qrcode`, `lokasi_id`) VALUES
(9, 'NH01', 'Laptop', 'Baik', 'Barang Masuk', 'Barang Habis Pakai', '12', '2021-07', 'Di Kembalikan', 'barang baru', 'foto/Walls_2.png', 'qr_codes/qrcode-NH01_O4FWbAu.png', 1),
(10, 'NH02', 'Laptop', 'Baik', 'Barang Masuk', 'Barang Habis Pakai', '12', '2021-12', 'Di Pinjam', 'barang baru', 'foto/09fb4d2c-e9d4-4949-b26d-969983c4bd54_169.jpeg', 'qr_codes/qrcode-NH001111_K0FkPRo.png', 2),
(11, 'NH03', 'Sepatu Siswa', 'Baik', 'Barang Masuk', 'Barang Habis Pakai', '2021-08-18', '2021-12', 'Di Kembalikan', 'barang baru', 'foto/download.jpg', 'qr_codes/qrcode-NH03.png', 1),
(12, 'NH04', 'Kipas Angin', NULL, 'Barang Masuk', NULL, NULL, NULL, 'Di Pinjam', 'Barang Siap Digunakan', 'foto/download_1.jpg', 'qr_codes/qrcode-NH04.png', 3);

-- --------------------------------------------------------

--
-- Struktur dari tabel `inventaris_cekbarang`
--

CREATE TABLE `inventaris_cekbarang` (
  `id` int(11) NOT NULL,
  `tanggal` datetime(6) DEFAULT NULL,
  `kode_barang_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktur dari tabel `inventaris_inventaris`
--

CREATE TABLE `inventaris_inventaris` (
  `id` int(11) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `status` varchar(150) DEFAULT NULL,
  `tanggalpinjam` date NOT NULL,
  `tanggalkembali` date NOT NULL,
  `barang_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `inventaris_inventaris`
--

INSERT INTO `inventaris_inventaris` (`id`, `nama`, `status`, `tanggalpinjam`, `tanggalkembali`, `barang_id`) VALUES
(5, 'gustin', 'Di Pinjam', '2021-08-18', '2021-12-12', 9),
(6, 'gustin', 'Di Kembalikan', '2021-08-19', '2021-12-12', 9);

-- --------------------------------------------------------

--
-- Struktur dari tabel `inventaris_petugas`
--

CREATE TABLE `inventaris_petugas` (
  `id` int(11) NOT NULL,
  `nama` varchar(30) NOT NULL,
  `nip` varchar(18) NOT NULL,
  `tempat_tanggal_lahir` varchar(50) NOT NULL,
  `pendidikan` varchar(30) NOT NULL,
  `email` varchar(30) NOT NULL,
  `alamat` varchar(50) NOT NULL,
  `no_hp` varchar(12) NOT NULL,
  `status` varchar(30) DEFAULT NULL,
  `foto` varchar(100) NOT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `inventaris_petugas`
--

INSERT INTO `inventaris_petugas` (`id`, `nama`, `nip`, `tempat_tanggal_lahir`, `pendidikan`, `email`, `alamat`, `no_hp`, `status`, `foto`, `user_id`) VALUES
(1, 'hikmah', '907782', 'malang, 12-01-2000', 'SMA', 'hikmah@gmail.com', 'Paiton', '082345678', 'Admin', 'fotokosong.jpg', 1),
(2, 'hikmahlagi', '907782', 'malang, 12-01-2000', 'SMA', 'sm04021999@gmail.com', 'Paiton', '0823456789', 'Admin', 'fotokosong.jpg', 2),
(3, 'tanti', '90778211', 'malang, 12-01-2000', 'SMA', 'fida@gmail.com', 'Paiton', '0823456789', 'Kepala Sekolah', 'fotokosong.jpg', 3),
(4, 'susan', '907782', 'malang, 12-01-2000', 'SMA', 'sm04021999@gmail.com', 'Paiton', '0823456789', 'Admin', 'fotokosong.jpg', 4);

-- --------------------------------------------------------

--
-- Struktur dari tabel `inventaris_pindahbarang`
--

CREATE TABLE `inventaris_pindahbarang` (
  `id` int(11) NOT NULL,
  `tanggal` datetime(6) DEFAULT NULL,
  `kode_barang_id` int(11) NOT NULL,
  `lokasi_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `inventaris_pindahbarang`
--

INSERT INTO `inventaris_pindahbarang` (`id`, `tanggal`, `kode_barang_id`, `lokasi_id`) VALUES
(4, '2021-08-18 16:16:00.079908', 10, 1),
(5, '2021-08-18 16:26:17.578409', 10, 3),
(6, '2021-08-18 16:40:56.399061', 10, 2),
(7, '2021-08-18 17:16:38.947564', 12, 3);

-- --------------------------------------------------------

--
-- Struktur dari tabel `inventaris_ruangan`
--

CREATE TABLE `inventaris_ruangan` (
  `id` int(11) NOT NULL,
  `kode_ruangan` varchar(50) NOT NULL,
  `nama_ruangan` varchar(50) NOT NULL,
  `keterangan` varchar(50) NOT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `inventaris_ruangan`
--

INSERT INTO `inventaris_ruangan` (`id`, `kode_ruangan`, `nama_ruangan`, `keterangan`, `user_id`) VALUES
(1, 'NH0012', 'Kelas XI', 'Kelas ini untuk siswa baru', 1),
(2, 'NH0011', 'Kelas VI', 'Kelas ini untuk siswa baru', 1),
(3, 'NH00113', 'Kelas VII', 'Kelas ini untuk siswa baru', 1),
(6, 'KR04', 'Ruangan Lab', 'Tempat untuk Barang elektronik', NULL);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `authtoken_token`
--
ALTER TABLE `authtoken_token`
  ADD PRIMARY KEY (`key`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indeks untuk tabel `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indeks untuk tabel `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indeks untuk tabel `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indeks untuk tabel `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indeks untuk tabel `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indeks untuk tabel `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indeks untuk tabel `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indeks untuk tabel `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indeks untuk tabel `inventaris_barang`
--
ALTER TABLE `inventaris_barang`
  ADD PRIMARY KEY (`id`),
  ADD KEY `inventaris_barang_lokasi_id_f487e78b_fk_inventaris_ruangan_id` (`lokasi_id`);

--
-- Indeks untuk tabel `inventaris_cekbarang`
--
ALTER TABLE `inventaris_cekbarang`
  ADD PRIMARY KEY (`id`),
  ADD KEY `inventaris_cekbarang_kode_barang_id_be2e5fe5_fk_inventari` (`kode_barang_id`);

--
-- Indeks untuk tabel `inventaris_inventaris`
--
ALTER TABLE `inventaris_inventaris`
  ADD PRIMARY KEY (`id`),
  ADD KEY `inventaris_inventaris_barang_id_0c471dac_fk_inventaris_barang_id` (`barang_id`);

--
-- Indeks untuk tabel `inventaris_petugas`
--
ALTER TABLE `inventaris_petugas`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indeks untuk tabel `inventaris_pindahbarang`
--
ALTER TABLE `inventaris_pindahbarang`
  ADD PRIMARY KEY (`id`),
  ADD KEY `inventaris_pindahbar_kode_barang_id_d77529dc_fk_inventari` (`kode_barang_id`),
  ADD KEY `inventaris_pindahbar_lokasi_id_4ac7d70c_fk_inventari` (`lokasi_id`);

--
-- Indeks untuk tabel `inventaris_ruangan`
--
ALTER TABLE `inventaris_ruangan`
  ADD PRIMARY KEY (`id`),
  ADD KEY `inventaris_ruangan_user_id_a887f949_fk_auth_user_id` (`user_id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT untuk tabel `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT untuk tabel `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT untuk tabel `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT untuk tabel `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT untuk tabel `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT untuk tabel `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT untuk tabel `inventaris_barang`
--
ALTER TABLE `inventaris_barang`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT untuk tabel `inventaris_cekbarang`
--
ALTER TABLE `inventaris_cekbarang`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `inventaris_inventaris`
--
ALTER TABLE `inventaris_inventaris`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT untuk tabel `inventaris_petugas`
--
ALTER TABLE `inventaris_petugas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT untuk tabel `inventaris_pindahbarang`
--
ALTER TABLE `inventaris_pindahbarang`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT untuk tabel `inventaris_ruangan`
--
ALTER TABLE `inventaris_ruangan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `authtoken_token`
--
ALTER TABLE `authtoken_token`
  ADD CONSTRAINT `authtoken_token_user_id_35299eff_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Ketidakleluasaan untuk tabel `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Ketidakleluasaan untuk tabel `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Ketidakleluasaan untuk tabel `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Ketidakleluasaan untuk tabel `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Ketidakleluasaan untuk tabel `inventaris_barang`
--
ALTER TABLE `inventaris_barang`
  ADD CONSTRAINT `inventaris_barang_lokasi_id_f487e78b_fk_inventaris_ruangan_id` FOREIGN KEY (`lokasi_id`) REFERENCES `inventaris_ruangan` (`id`);

--
-- Ketidakleluasaan untuk tabel `inventaris_cekbarang`
--
ALTER TABLE `inventaris_cekbarang`
  ADD CONSTRAINT `inventaris_cekbarang_kode_barang_id_be2e5fe5_fk_inventari` FOREIGN KEY (`kode_barang_id`) REFERENCES `inventaris_barang` (`id`);

--
-- Ketidakleluasaan untuk tabel `inventaris_inventaris`
--
ALTER TABLE `inventaris_inventaris`
  ADD CONSTRAINT `inventaris_inventaris_barang_id_0c471dac_fk_inventaris_barang_id` FOREIGN KEY (`barang_id`) REFERENCES `inventaris_barang` (`id`);

--
-- Ketidakleluasaan untuk tabel `inventaris_petugas`
--
ALTER TABLE `inventaris_petugas`
  ADD CONSTRAINT `inventaris_petugas_user_id_de6210a6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Ketidakleluasaan untuk tabel `inventaris_pindahbarang`
--
ALTER TABLE `inventaris_pindahbarang`
  ADD CONSTRAINT `inventaris_pindahbar_kode_barang_id_d77529dc_fk_inventari` FOREIGN KEY (`kode_barang_id`) REFERENCES `inventaris_barang` (`id`),
  ADD CONSTRAINT `inventaris_pindahbar_lokasi_id_4ac7d70c_fk_inventari` FOREIGN KEY (`lokasi_id`) REFERENCES `inventaris_ruangan` (`id`);

--
-- Ketidakleluasaan untuk tabel `inventaris_ruangan`
--
ALTER TABLE `inventaris_ruangan`
  ADD CONSTRAINT `inventaris_ruangan_user_id_a887f949_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
